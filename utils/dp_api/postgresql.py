import asyncio
import asyncpg
import config
from asyncpg import Pool
from typing import Union


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        pool = await asyncpg.create_pool(
            user=config.PGUSER,
            password=config.PGPASSWORD,
            host=config.IP,

        )
        self.pool = pool

    async def create_table_with_questions_litra(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_litra (
        id SERIAL,
        question VARCHAR(255) NOT NULL,
        first VARCHAR(255) NOT NULL,
        second VARCHAR(255) NOT NULL,
        third VARCHAR(255) NOT NULL,
        fourth VARCHAR(255) NOT NULL,
        fifth VARCHAR(255) NOT NULL,
        correct INT NOT NULL
        );
        """
        await self.pool.execute(sql)

    async def create_table_with_questions_mova(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_mova (
        id SERIAL,
        question VARCHAR(255) NOT NULL,
        first VARCHAR(255) NOT NULL,
        second VARCHAR(255) NOT NULL,
        third VARCHAR(255) NOT NULL,
        fourth VARCHAR(255) NOT NULL,
        correct INT NOT NULL
        );
        """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_question_to_litra(self, question: str, first: str, second: str, third: str, fourth: str, fifth: str,
                           correct: int):
        sql = """INSERT INTO Questions_litra (question, first, second, third, fourth, fifth, correct)
            VALUES ($1,$2,$3,$4,$5,$6,$7)"""
        await self.pool.execute(sql, question, first, second, third, fourth, fifth, correct)

    async def add_question_to_mova(self, question: str, first: str, second: str, third: str, fourth: str,
                           correct: int):
        sql = """INSERT INTO Questions_mova (question, first, second, third, fourth, correct)
            VALUES ($1,$2,$3,$4,$5,$6)"""
        await self.pool.execute(sql, question, first, second, third, fourth, correct)

    async def select_all_questions_litra(self):
        sql = "SELECT * FROM Questions_litra"
        return await self.pool.fetch(sql)

    async def select_all_questions_mova(self):
        sql = "SELECT * FROM Questions_mova"
        return await self.pool.fetch(sql)


    async def delete_questions(self):
        await self.pool.execute("DELETE FROM Questions_litra WHERE True")
        await self.pool.execute("DELETE FROM Questions_mova WHERE TRUE")
