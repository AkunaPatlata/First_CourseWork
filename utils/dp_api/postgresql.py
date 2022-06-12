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

    async def create_table_with_questions_for_nagolos(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_mova_nagolos (
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

    async def create_table_with_questions_for_apostrof(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_mova_apostrof (
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

    async def create_table_with_questions_for_skladni(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_mova_skladni (
        id SERIAL,
        question VARCHAR(500) NOT NULL,
        first VARCHAR(255) NOT NULL,
        second VARCHAR(255) NOT NULL,
        third VARCHAR(255) NOT NULL,
        fourth VARCHAR(255) NOT NULL,
        fifth VARCHAR(255) NOT NULL,
        correct INT NOT NULL
        );
        """
        await self.pool.execute(sql)

    async def create_table_with_questions_for_double(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_mova_double (
        id SERIAL,
        question VARCHAR(500) NOT NULL,
        first VARCHAR(255) NOT NULL,
        second VARCHAR(255) NOT NULL,
        third VARCHAR(255) NOT NULL,
        fourth VARCHAR(255) NOT NULL,
        fifth VARCHAR(255) NOT NULL,
        correct INT NOT NULL
        );
        """
        await self.pool.execute(sql)

    async def create_table_with_questions_for_foreign(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_mova_foreign (
        id SERIAL,
        question VARCHAR(500) NOT NULL,
        first VARCHAR(255) NOT NULL,
        second VARCHAR(255) NOT NULL,
        third VARCHAR(255) NOT NULL,
        fourth VARCHAR(255) NOT NULL,
        fifth VARCHAR(255) NOT NULL,
        correct INT NOT NULL
        );
        """
        await self.pool.execute(sql)

    async def create_table_with_questions_for_prefiks(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Questions_mova_prefiks (
        id SERIAL,
        question VARCHAR(500) NOT NULL,
        first VARCHAR(255) NOT NULL,
        second VARCHAR(255) NOT NULL,
        third VARCHAR(255) NOT NULL,
        fourth VARCHAR(255) NOT NULL,
        fifth VARCHAR(255) NOT NULL,
        correct INT NOT NULL
        );
        """
        await self.pool.execute(sql)

    async def add_questions_to_mova_skladni(self, question: str, first: str, second: str, third: str, fourth: str,
                                            fifth: str,
                                            correct: int):
        sql = """INSERT INTO Questions_mova_skladni (question, first, second, third, fourth, fifth, correct)
                    VALUES ($1,$2,$3,$4,$5,$6,$7)"""
        await self.pool.execute(sql, question, first, second, third, fourth, fifth, correct)

    async def add_questions_to_mova_foreign(self, question: str, first: str, second: str, third: str, fourth: str,
                                            fifth: str,
                                            correct: int):
        sql = """INSERT INTO Questions_mova_foreign (question, first, second, third, fourth, fifth, correct)
                    VALUES ($1,$2,$3,$4,$5,$6,$7)"""
        await self.pool.execute(sql, question, first, second, third, fourth, fifth, correct)

    async def add_questions_to_mova_double(self, question: str, first: str, second: str, third: str, fourth: str,
                                           fifth: str,
                                           correct: int):
        sql = """INSERT INTO Questions_mova_double (question, first, second, third, fourth, fifth, correct)
                    VALUES ($1,$2,$3,$4,$5,$6,$7)"""
        await self.pool.execute(sql, question, first, second, third, fourth, fifth, correct)

    async def add_questions_to_mova_nagolos(self, question: str, first: str, second: str, third: str, fourth: str,
                                            correct: int):
        sql = """INSERT INTO Questions_mova_nagolos (question, first, second, third, fourth, correct)
                    VALUES ($1,$2,$3,$4,$5,$6)"""
        await self.pool.execute(sql, question, first, second, third, fourth, correct)

    async def add_questions_to_mova_prefiks(self, question: str, first: str, second: str, third: str, fourth: str,
                                            fifth: str,
                                            correct: int):
        sql = """INSERT INTO Questions_mova_prefiks (question, first, second, third, fourth, fifth, correct)
                    VALUES ($1,$2,$3,$4,$5,$6,$7)"""
        await self.pool.execute(sql, question, first, second, third, fourth, fifth, correct)

    async def add_questions_to_mova_apostrof(self, question: str, first: str, second: str, third: str, fourth: str,
                                             fifth: str,
                                             correct: int):
        sql = """INSERT INTO Questions_mova_apostrof (question, first, second, third, fourth, fifth, correct)
                    VALUES ($1,$2,$3,$4,$5,$6,$7)"""
        await self.pool.execute(sql, question, first, second, third, fourth, fifth, correct)

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

    async def select_all_questions_nagolos(self):
        sql = "SELECT * FROM Questions_mova_nagolos"
        return await self.pool.fetch(sql)

    async def select_all_questions_skladni(self):
        sql = "SELECT * FROM Questions_mova_skladni"
        return await self.pool.fetch(sql)

    async def select_all_questions_double(self):
        sql = "SELECT * FROM Questions_mova_double"
        return await self.pool.fetch(sql)

    async def select_all_questions_apostrof(self):
        sql = "SELECT * FROM Questions_mova_apostrof"
        return await self.pool.fetch(sql)

    async def select_all_questions_foreign(self):
        sql = "SELECT * FROM Questions_mova_foreign"
        return await self.pool.fetch(sql)

    async def select_all_questions_prefiks(self):
        sql = "SELECT * FROM Questions_mova_prefiks"
        return await self.pool.fetch(sql)

    async def delete_questions(self):
        await self.pool.execute("DELETE FROM Questions_litra WHERE True")
        await self.pool.execute("DELETE FROM Questions_mova WHERE TRUE")
        await self.pool.execute("DELETE FROM Questions_mova_nagolos WHERE TRUE")
        await self.pool.execute("DELETE FROM Questions_mova_prefiks WHERE TRUE")
        await self.pool.execute("DELETE FROM Questions_mova_double WHERE TRUE")
        await self.pool.execute("DELETE FROM Questions_mova_skladni WHERE TRUE")
        await self.pool.execute("DELETE FROM Questions_mova_apostrof WHERE TRUE")
        await self.pool.execute("DELETE FROM Questions_mova_foreign WHERE TRUE")
