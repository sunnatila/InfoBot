import datetime
import sqlite3


class Database:
    def __init__(self, db_name='db.sqlite3'):
        self.db_name = db_name

    @property
    def connect(self):
        return sqlite3.connect(self.db_name)

    # connect database
    # --------------------------------------------------------------------------------------------------------
    # Get something from database

    async def get_company_info(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                SELECT general_info_uz, history_uz, mission_uz, company_vision_uz, image_url FROM companies
            """
            res = cur.execute(query)
            return res.fetchone()
        else:
            query = """
                    SELECT general_info_ru, history_ru, mission_ru, company_vision_ru, image_url FROM companies
            """
            res = cur.execute(query)
            return res.fetchone()

    async def get_news_title(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                SELECT id, title_uz FROM news
            """
            res = cur.execute(query)
            return res.fetchall()
        else:
            query = """
                    SELECT id, title_ru FROM news
            """
            res = cur.execute(query)
            return res.fetchall()

    async def get_news_info(self, lang, news_id):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                SELECT id, title_uz, body_uz, image_url FROM news where id=?
            """
            res = cur.execute(query, (news_id,))
            return res.fetchone()
        else:
            query = """
                    SELECT id, title_ru, body_ru, image_url FROM news where id=?
            """
            res = cur.execute(query, (news_id,))
            return res.fetchone()

    async def get_user_from_id(self, user_id):
        con = self.connect
        cur = con.cursor()
        query = """
                    SELECT language FROM tg_users where tg_id=?
                """
        resp = cur.execute(query, (user_id,))

        return resp.fetchone()

    async def get_invest_info(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                        SELECT financial_info_uz, reports_uz, future_plan_uz, contact_info_uz, image_url FROM investors
                    """
            resp = cur.execute(query)
            if resp:
                return resp.fetchone()
            else:
                return []
        else:
            query = """
                        SELECT financial_info_ru, reports_ru, future_plan_ru, contact_info_ru, image_url FROM investors
            """
            resp = cur.execute(query)
            if resp:
                return resp.fetchone()
            else:
                return []

    async def get_service_info(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                        SELECT service_uz, product_uz FROM services
                    """
            resp = cur.execute(query)
            if resp == None:
                return []
            else:
                return resp.fetchone()
        else:
            query = """
                        SELECT service_ru, product_ru FROM services
            """
            resp = cur.execute(query)
            if resp == None:
                return []

            else:
                return resp.fetchone()

    async def get_partners_info(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                    SELECT partnership_opportunities_uz, partnership_programs_uz, conditions_uz, 
                    contact_info_uz, image_url 
                    FROM partners
                """
            resp = cur.execute(query)
            if resp == None:
                return []
            else:
                return resp.fetchone()
        else:
            query = """
                    SELECT partnership_opportunities_ru, partnership_programs_ru, conditions_ru, 
                    contact_info_ru, image_url  
                    FROM partners
                    """
            resp = cur.execute(query)
            if resp == None:
                return []

            else:
                return resp.fetchone()

    async def get_company_location(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                    SELECT company_address_uz FROM contacts
                    
                """
            resp = cur.execute(query)
            return resp.fetchone()
        else:
            query = """
                    SELECT company_address_ru FROM contacts
                    """
            resp = cur.execute(query)
            return resp.fetchone()

    async def get_company_contact(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                    SELECT phone_number_uz FROM contacts

                """
            resp = cur.execute(query)
            return resp.fetchone()
        else:
            query = """
                    SELECT phone_number_ru FROM contacts
                    """
            resp = cur.execute(query)
            return resp.fetchone()

    async def get_company_email(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                    SELECT email_uz FROM contacts

                """
            resp = cur.execute(query)
            return resp.fetchone()
        else:
            query = """
                    SELECT email_ru FROM contacts
                    """
            resp = cur.execute(query)
            return resp.fetchone()

    async def get_company_social_networks(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                    SELECT social_networks_uz FROM contacts

                """
            resp = cur.execute(query)
            return resp.fetchone()
        else:
            query = """
                    SELECT social_networks_ru FROM contacts
                    """
            resp = cur.execute(query)
            return resp.fetchone()

    async def get_faq_questions(self, lang):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                    SELECT id, question_uz FROM questions

                """
            resp = cur.execute(query)
            return resp.fetchall()
        else:
            query = """
                    SELECT id, question_ru FROM questions
                    """
            resp = cur.execute(query)
            return resp.fetchall()

    async def get_faq_answers(self, lang, question_id):
        con = self.connect
        cur = con.cursor()
        if lang == 'uz':
            query = """
                    SELECT question_uz, answer_uz FROM questions where id=?

                """
            resp = cur.execute(query, (question_id,))
            return resp.fetchone()
        else:
            query = """
                    SELECT question_ru, answer_ru FROM questions where id=?
                    """
            resp = cur.execute(query, (question_id,))
            return resp.fetchone()

    # --------------------------------------------------------------------------------------------------------

    # Add users

    async def add_tg_user(self, lang, user_id):
        con = self.connect
        cur = con.cursor()
        query = """
                    INSERT INTO tg_users(language, tg_id)
                    VALUES (?, ?)
                """
        res = cur.execute(query, (lang, user_id))
        if res:
            print("Foydalanuvchi muvaffaqiyatli qoshildi.")
            con.commit()
        else:
            print("Foydalanuvchi qoshishda hatolik")

    async def add_invest_user(self, fullname, phone, advice):
        con = self.connect
        cur = con.cursor()
        query = """
                    INSERT INTO invest_applications(fullname, phone, advice, create_at, updated_at)
                    VALUES (?, ?, ?, ?, ?)
                """
        res = cur.execute(query, (fullname, phone, advice, datetime.datetime.now().date(), datetime.datetime.now().date()))
        if res:
            print("Foydalanuvchi muvaffaqiyatli qoshildi.")
            con.commit()
        else:
            print("Foydalanuvchi qoshishda hatolik")

    async def add_partner(self, fullname, phone, advice):
        con = self.connect
        cur = con.cursor()
        query = """
                            INSERT INTO partner_applications(fullname, phone, advice, create_at, updated_at)
                            VALUES (?, ?, ?, ?, ?)
                        """
        res = cur.execute(query,
                          (fullname, phone, advice, datetime.datetime.now().date(), datetime.datetime.now().date()))
        if res:
            print("Foydalanuvchi muvaffaqiyatli qoshildi.")
            con.commit()
        else:
            print("Foydalanuvchi qoshishda hatolik")

    #--------------------------------------------------------------------------------------------------------

    # Update users

    async def update_user(self, lang: str, tg_id: int):
        con = self.connect
        cur = con.cursor()
        query = """
            UPDATE tg_users SET language=? WHERE tg_id=?
        """
        try:
            cur.execute(query, (lang, tg_id))
            con.commit()
            print("Foydalanuvchi muvaffaqiyatli ozgartirildi.")
        except sqlite3.Error as e:
            print(f"Xatolik: {e}")
