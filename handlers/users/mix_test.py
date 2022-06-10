from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.callback_data import CallbackData
import random
from loader import dp, db
from states.states import Test

cb_get_mix_answers = CallbackData("get_mix_answers", "answer_id")


@dp.message_handler(Command('start_mix_test'), state="*")
async def get_15_random_questions_mix(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    questions_litra = await db.select_all_questions_litra()
    questions_mova = await db.select_all_questions_mova()
    questions_litra = [dict(q) for q in random.sample(questions_litra, 8)]
    questions_mova = [dict(q) for q in random.sample(questions_mova, 7)]
    questions_mix = questions_mova + questions_litra
    question = questions_mix.pop(0)
    question_text = question.get("question")
    correct = question.get("correct")
    counter = 0
    print(correct)
    if question.get("fifth"):
        variables = [question.get("first"), question.get("second"), question.get("third"),
                     question.get("fourth"), question.get("fifth")]
    else:
        variables = [question.get("first"), question.get("second"), question.get("third"),
                     question.get("fourth")]
    for index, variable in enumerate(variables, start=1):
        keyboard.add(types.InlineKeyboardButton(text=variable,
                                                callback_data=cb_get_mix_answers.new(answer_id=index)))

    await message.answer(f"№{15 - len(questions_mix)}\n ⚡{question_text}⚡", reply_markup=keyboard)
    await state.update_data(variables=variables)
    await state.update_data(correct=correct)
    await state.update_data(questions=questions_mix)
    await state.update_data(counter=counter)
    await Test.Mix.set()


@dp.callback_query_handler(cb_get_mix_answers.filter(), state=Test.Mix)
async def get_lit_answers_call(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    questions = data.get('questions')
    answer_id = int(callback_data["answer_id"])
    counter = data.get('counter')
    correct = data.get('correct')
    variables = data.get('variables')
    if answer_id == correct:
        await call.message.answer("✅Правильна відповідь✅\n"
                                  f"Ви обрали варіант: «{variables[answer_id - 1]}»")
        await call.message.edit_reply_markup()
        counter += 1
        await state.update_data(counter=counter)
    else:
        await call.message.answer("⛔Неправильна відповідь⛔\n"
                                  f"Ви обрали варіант: «{variables[answer_id - 1]}»\n"
                                  f"Правильна відповідь: «{variables[correct - 1]}»")
        await call.message.edit_reply_markup()
    print(answer_id, correct)
    if questions:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        question = questions.pop(0)
        question_text = question.get("question")
        correct = question.get("correct")
        print(correct)
        if question.get("fifth"):
            variables = [question.get("first"), question.get("second"), question.get("third"),
                         question.get("fourth"), question.get("fifth")]
        else:
            variables = [question.get("first"), question.get("second"), question.get("third"),
                         question.get("fourth")]
        for index, variable in enumerate(variables, start=1):
            keyboard.add(types.InlineKeyboardButton(text=variable,
                                                    callback_data=cb_get_mix_answers.new(answer_id=index)))
        await call.message.answer(f"№{15 - len(questions)}\n ⚡{question_text}⚡", reply_markup=keyboard)
        await state.update_data(variables=variables)
        await state.update_data(correct=correct)
        await state.update_data(questions=questions)
    else:
        if counter != 0:
            await call.message.answer(f"Вітаю! Ви набрали {counter} / 15")
            if counter == 15:
                await call.message.answer("Це ідеальний результат! Так тримати!")
            if counter >= 12:
                await call.message.answer("Це дуже хороший результат! Ще трохи попрацювати😮‍💨 і буде ідеально!")
            if counter >= 7 and counter < 12:
                await call.message.answer("Ти молодець, це хороший результат!👍")
            if counter >= 4 and counter < 7:
                await call.message.answer(
                    "Твій результат, нажаль, далекий від ідеалу, але все ще попереду, я в тебе вірю!😉")
            if counter < 4:
                await call.message.answer("Нажаль це низький рівень😢\nАле все в твоїх руках, ще є час виправитися!")
        else:
            await call.message.answer(
                "Шкода... Ви набрали 0 балів😔\nАле я вірю в тебе, ще трішки попрацювати і результат точно буде кращим!")
        await state.finish()

    await call.answer(cache_time=60)
