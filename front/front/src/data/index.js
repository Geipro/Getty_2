export default {
    User: [
        {
            user_id: 1,
            name: 'lelana',
            created_at : '2018-09-11 11:42:11'
        },
        {
            user_id: 2,
            name: 'Irin',
            created_at : '2018-09-11 11:42:11'
        },
        {
            user_id: 3,
            name: 'Joy',
            created_at : '2018-09-11 11:42:11'
        },
    ],
    Content: [
        {
            content_id: 1,
            user_id: 1,
            title: "안녕하세요 반가워요",
            context: "방금 가입했어요~",
            created_at : '2019-01-01 13:13:12'
        },
        {
            content_id: 2,
            user_id: 3,
            title: "안녕하세요!",
            context: "잘 부탁드려요",
            created_at : '2019-01-02 13:13:12'
        },
        {
            content_id: 3,
            user_id: 2,
            title: "오늘은 제 생일이에요",
            context: "축하해주세요~",
            created_at : '2019-07-06 13:13:12'
        }
    ],
    Comment: [
        {
            comment_id: 1,
            user_id: 1,
            content_id: 3,
            context: "생일축하해요!",
            created_at: '2019-07-06 14:02:00',
            updated_at : null
        },
        {
            comment_id: 2,
            user_id: 3,
            content_id: 3,
            context: "와! 정말 생일축하해요!",
            created_at: '2019-07-06 14:05:00',
            updated_at : null
        },
        {
            comment_id: 3,
            user_id: 2,
            content_id: 1,
            context: "잘 보고 있습니다!",
            created_at: '2019-01-02 14:02:00',
            updated_at : null
        }
    ]
}