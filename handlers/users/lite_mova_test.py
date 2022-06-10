from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.callback_data import CallbackData
import random
from loader import dp, db
from states.states import Test

cb_get_mova_answers = CallbackData("get_mova_answers", "answer_id")


@dp.message_handler(Command('start_lite_mova'), state="*")
async def get_10_random_questions_mova(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    questions = await db.select_all_questions_mova()
    questions = [dict(q) for q in random.sample(questions, 11)]
    question = questions.pop(0)
    question_text = question.get("question")
    correct = question.get("correct")
    counter = 0
    print(correct)
    variables = [question.get("first"), question.get("second"), question.get("third"),
                 question.get("fourth")]
    for index, variable in enumerate(variables, start=1):
        keyboard.add(types.InlineKeyboardButton(text=variable,
                                                callback_data=cb_get_mova_answers.new(answer_id=index)))

    await message.answer(f"№{11 - len(questions)}\n ⚡{question_text}⚡", reply_markup=keyboard)
    await state.update_data(variables=variables)
    await state.update_data(correct=correct)
    await state.update_data(questions=questions)
    await state.update_data(counter=counter)
    await Test.Mova.set()


@dp.callback_query_handler(cb_get_mova_answers.filter(), state=Test.Mova)
async def get_mova_answers_call(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    questions = data.get('questions')
    answer_id = int(callback_data["answer_id"])
    counter = data.get('counter')
    correct = data.get('correct')
    variables = data.get('variables')
    question = questions.pop(0)

    if answer_id == correct:
        await call.message.answer("✅Правильна відповідь✅\n"
                                  f"Ви обрали варіант: «{variables[answer_id-1]}»")
        await call.message.edit_reply_markup()
        counter += 1
        await state.update_data(counter=counter)
    else:
        await call.message.answer("⛔Неправильна відповідь⛔\n"
                                  f"Ви обрали варіант: «{variables[answer_id-1]}»\n"
                                  f"Правильна відповідь: «{variables[correct-1]}»")
        await call.message.edit_reply_markup()
    print(answer_id, correct)
    if questions:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        question_text = question.get("question")
        correct = question.get("correct")
        print(correct)
        variables = [question.get("first"), question.get("second"), question.get("third"),
                     question.get("fourth")]
        for index, variable in enumerate(variables, start=1):
            keyboard.add(types.InlineKeyboardButton(text=variable,
                                                    callback_data=cb_get_mova_answers.new(answer_id=index)))
        await call.message.answer(f"№{11 - len(questions)}\n ⚡{question_text}⚡", reply_markup=keyboard)
        await state.update_data(variables=variables)
        await state.update_data(correct=correct)
        await state.update_data(questions=questions)
    else:
        if counter != 0:
            await call.message.answer(f"Вітаю! Ви набрали {counter} / 10")
            if counter == 10:
                await call.message.answer("Це ідеальний результат! Так тримати!")
        else:
            await call.message.answer(
                "Шкода... Ви набрали 0 балів😔\nАле я вірю в тебе, ще трішки попрацювати і результат точно буде кращим!")
    await call.answer(cache_time=60)
