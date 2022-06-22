from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.callback_data import CallbackData
import random
from loader import dp, db
from states.states import Test

cb_get_game_answers = CallbackData("get_game_answers", "answer_id")


@dp.message_handler(Command('game_test'), state="*")
async def get_questions_for_game(message: types.Message, state: FSMContext):
    await message.answer(
        "Давай зіграємо в гру👾\nПравила досить прості: в тебе є 3 життя, 1 життя = 1 помилка. Спробуй пройти якомога більше тестів і вижити, успіхів☺")
    name = message.from_user.full_name
    user_id = message.from_user.id
    results_from_db = await db.select_all_results()
    results_from_db = [list(q) for q in results_from_db]
    results = []
    for i in results_from_db:
        if i != [None]:
            results.append(i)
    max_res = max(results)[0]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    questions_litra = await db.select_all_questions_litra()
    questions_mova = await db.select_all_questions_mova()
    questions_litra = [dict(q) for q in random.sample(questions_litra, 45)]
    questions_mova = [dict(q) for q in random.sample(questions_mova, 45)]
    questions_mix = questions_mova + questions_litra
    questions_mix = [dict(q) for q in random.sample(questions_mix, 90)]
    question = questions_mix.pop(0)
    question_text = question.get("question")
    correct = question.get("correct")
    counter_for_true = 0
    counter_for_false = 0
    print(correct)
    if question.get("fifth"):
        variables = [question.get("first"), question.get("second"), question.get("third"),
                     question.get("fourth"), question.get("fifth")]
    else:
        variables = [question.get("first"), question.get("second"), question.get("third"),
                     question.get("fourth")]
    for index, variable in enumerate(variables, start=1):
        keyboard.add(types.InlineKeyboardButton(text=variable,
                                                callback_data=cb_get_game_answers.new(answer_id=index)))

    await message.answer(f"№{90 - len(questions_mix)}\n ⚡{question_text}⚡", reply_markup=keyboard)
    await state.update_data(user_id=user_id)
    await state.update_data(variables=variables)
    await state.update_data(correct=correct)
    await state.update_data(questions=questions_mix)
    await state.update_data(counter_for_true=counter_for_true)
    await state.update_data(counter_for_false=counter_for_false)
    await state.update_data(max_res=max_res)
    await state.update_data(name=name)
    await Test.Mix.set()


@dp.callback_query_handler(cb_get_game_answers.filter(), state=Test.Mix)
async def get_lit_answers_call(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    counter_for_false = data.get('counter_for_false')
    counter_for_true = data.get('counter_for_true')
    questions = data.get('questions')
    user_id = data.get('user_id')
    max_res = data.get('max_res')
    name = data.get('name')
    answer_id = int(callback_data["answer_id"])
    correct = data.get('correct')
    variables = data.get('variables')
    if answer_id == correct:
        if counter_for_false == 0:
            await call.message.answer("✅Правильна відповідь✅\n"
                                      f"Ви обрали варіант: «{variables[answer_id - 1]}»\n"
                                      f"❤❤❤")
        elif counter_for_false == 1:
            await call.message.answer("✅Правильна відповідь✅\n"
                                      f"Ви обрали варіант: «{variables[answer_id - 1]}»\n"
                                      f"❤❤💔")
        elif counter_for_false == 2:
            await call.message.answer("✅Правильна відповідь✅\n"
                                      f"Ви обрали варіант: «{variables[answer_id - 1]}»\n"
                                      f"❤💔💔")

        await call.message.edit_reply_markup()
        counter_for_true += 1
        await state.update_data(counter_for_true=counter_for_true)
    else:
        counter_for_false += 1
        if counter_for_false == 1:
            await call.message.answer("⛔Неправильна відповідь⛔\n"
                                      f"Ви обрали варіант: «{variables[answer_id - 1]}»\n"
                                      f"Правильна відповідь: «{variables[correct - 1]}»\n"
                                      f"Ви втратили одне життя: ❤❤💔")
        elif counter_for_false == 2:
            await call.message.answer("⛔Неправильна відповідь⛔\n"
                                      f"Ви обрали варіант: «{variables[answer_id - 1]}»\n"
                                      f"Правильна відповідь: «{variables[correct - 1]}»\n"
                                      f"Ви втратили одне життя: ❤💔💔")
        await state.update_data(counter_for_false=counter_for_false)
        await call.message.edit_reply_markup()
    print(answer_id, correct)
    if counter_for_false != 3:
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
                                                        callback_data=cb_get_game_answers.new(answer_id=index)))
            await call.message.answer(f"№{90 - len(questions)}\n ⚡{question_text}⚡", reply_markup=keyboard)
            await state.update_data(variables=variables)
            await state.update_data(correct=correct)
            await state.update_data(questions=questions)
        else:
            await call.message.answer(
                "Вітаю чемпіоне🏆, ти набрав максимально можливий бал і вижив, зно на 200 гарантовано!")
            await state.finish()
    else:
        await call.message.answer(f'Нажаль ви втратили всі життя😢. Ваш фінальний результат: {counter_for_true}')
        await db.add_user(id=user_id, name=name, result=0)
        db_result = await db.select_specific_result(id=user_id)
        if counter_for_true > max_res:
            await call.message.answer('Вітаємо🥳\nЦе абсолютний рекорд в нашому боті, ти молодець💪')
        if not db_result.get('result') or db_result.get('result') < counter_for_true:
            await db.update_user_result(counter_for_true, user_id)

        await state.finish()
    await call.answer(cache_time=60)
