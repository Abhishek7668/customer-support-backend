from repositry.analytics_repositry import AnalyticsRepository


class AnalyticsService:

    @staticmethod
    async def overview():

        conversations = await AnalyticsRepository.total_conversations()

        sessions = await AnalyticsRepository.total_sessions()

        users = await AnalyticsRepository.total_users()

        escalations = await AnalyticsRepository.escalated_cases()

        return {

            "total_users": users,

            "total_sessions": sessions,

            "total_conversations": conversations,

            "total_escalations": escalations

        }
    @staticmethod
    async def agent_usage():

        return await AnalyticsRepository.agent_usage()
    
    @staticmethod
    async def intent_usage():

        return await AnalyticsRepository.intent_usage()
    
    @staticmethod
    async def session_usage():

        return await AnalyticsRepository.session_usage()
    @staticmethod
    async def escalation_summary():

        return await AnalyticsRepository.escalation_summary()