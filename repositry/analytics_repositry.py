from core.database import get_database


class AnalyticsRepository:

    @staticmethod
    async def total_conversations():

        db = get_database()

        return await db.conversations.count_documents({})


    @staticmethod
    async def total_sessions():

        db = get_database()

        return await db.sessions.count_documents({})


    @staticmethod
    async def total_users():

        db = get_database()

        return await db.users.count_documents({})


    @staticmethod
    async def escalated_cases():

        db = get_database()

        return await db.conversations.count_documents(

            {

                "escalate": True

            }

        )
    @staticmethod
    async def agent_usage():

        db = get_database()

        pipeline = [

            {
                "$group": {

                    "_id": "$agent",

                    "count": {

                        "$sum": 1

                    }

                }

            },

            {

                "$sort": {

                    "count": -1

                }

            }

        ]

        result = []

        async for item in db.conversations.aggregate(pipeline):

            result.append({

                "agent": item["_id"],

                "count": item["count"]

            })

        return result
    @staticmethod
    async def intent_usage():

        db = get_database()

        pipeline = [

            {
                "$group": {

                    "_id": "$intent",

                    "count": {

                        "$sum": 1

                    }

                }

            },

            {

                "$sort": {

                    "count": -1

                }

            }

        ]

        result = []

        async for item in db.conversations.aggregate(pipeline):

            result.append({

                "intent": item["_id"],

                "count": item["count"]

            })

        return result
    @staticmethod
    async def session_usage():

        db = get_database()

        pipeline = [

            {
                "$group": {

                    "_id": "$session_id",

                    "messages": {

                        "$sum": 1

                    }

                }

            },

            {

                "$sort": {

                    "messages": -1

                }

            }

        ]

        result = []

        async for item in db.conversations.aggregate(pipeline):

            result.append({

                "session_id": item["_id"],

                "messages": item["messages"]

            })

        return result
    
    @staticmethod
    async def escalation_summary():

        db = get_database()

        pipeline = [

            {

                "$group": {

                    "_id": "$priority",

                    "count": {

                        "$sum": 1

                    }

                }

            }

        ]

        summary = {

            "HIGH": 0,

            "MEDIUM": 0,

            "LOW": 0

        }

        async for item in db.conversations.aggregate(pipeline):

            summary[item["_id"]] = item["count"]

        total = sum(summary.values())

        escalated = summary["HIGH"]

        return {

            "total_conversations": total,

            "high_priority": summary["HIGH"],

            "medium_priority": summary["MEDIUM"],

            "low_priority": summary["LOW"],

            "total_escalations": escalated

        }