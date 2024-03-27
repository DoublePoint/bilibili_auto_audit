import json
import jsonpath

data = '''{
    "code": 0,
    "message": "0",
    "ttl": 1,
    "data": {
        "isLogin": true,
        "email_verified": 0,
        "face": "https://i0.hdslb.com/bfs/face/971cd8dfb1314ddb8da819d0f5bb45ea6354cb72.jpg",
        "face_nft": 0,
        "face_nft_type": 0,
        "level_info": {
            "current_level": 3,
            "current_min": 1500,
            "current_exp": 2990,
            "next_exp": 4500
        },
        "mid": 3493136082930546,
        "mobile_verified": 1,
        "money": 275.7,
        "moral": 70,
        "official": {
            "role": 0,
            "title": "",
            "desc": "",
            "type": -1
        },
        "officialVerify": {
            "type": -1,
            "desc": ""
        },
        "pendant": {
            "pid": 0,
            "name": "",
            "image": "",
            "expire": 0,
            "image_enhance": "",
            "image_enhance_frame": "",
            "n_pid": 0
        },
        "scores": 0,
        "uname": "小艳儿咩",
        "vipDueDate": 0,
        "vipStatus": 0,
        "vipType": 0,
        "vip_pay_type": 0,
        "vip_theme_type": 0,
        "vip_label": {
            "path": "",
            "text": "",
            "label_theme": "",
            "text_color": "",
            "bg_style": 0,
            "bg_color": "",
            "border_color": "",
            "use_img_label": true,
            "img_label_uri_hans": "",
            "img_label_uri_hant": "",
            "img_label_uri_hans_static": "https://i0.hdslb.com/bfs/vip/d7b702ef65a976b20ed854cbd04cb9e27341bb79.png",
            "img_label_uri_hant_static": "https://i0.hdslb.com/bfs/activity-plat/static/20220614/e369244d0b14644f5e1a06431e22a4d5/KJunwh19T5.png"
        },
        "vip_avatar_subscript": 0,
        "vip_nickname_color": "",
        "vip": {
            "type": 0,
            "status": 0,
            "due_date": 0,
            "vip_pay_type": 0,
            "theme_type": 0,
            "label": {
                "path": "",
                "text": "",
                "label_theme": "",
                "text_color": "",
                "bg_style": 0,
                "bg_color": "",
                "border_color": "",
                "use_img_label": true,
                "img_label_uri_hans": "",
                "img_label_uri_hant": "",
                "img_label_uri_hans_static": "https://i0.hdslb.com/bfs/vip/d7b702ef65a976b20ed854cbd04cb9e27341bb79.png",
                "img_label_uri_hant_static": "https://i0.hdslb.com/bfs/activity-plat/static/20220614/e369244d0b14644f5e1a06431e22a4d5/KJunwh19T5.png"
            },
            "avatar_subscript": 0,
            "nickname_color": "",
            "role": 0,
            "avatar_subscript_url": "",
            "tv_vip_status": 0,
            "tv_vip_pay_type": 0,
            "tv_due_date": 0,
            "avatar_icon": {
                "icon_resource": {}
            }
        },
        "wallet": {
            "mid": 3493136082930546,
            "bcoin_balance": 0,
            "coupon_balance": 0,
            "coupon_due_time": 0
        },
        "has_shop": false,
        "shop_url": "",
        "allowance_count": 0,
        "answer_status": 0,
        "is_senior_member": 0,
        "wbi_img": {
            "img_url": "https://i0.hdslb.com/bfs/wbi/7cd084941338484aae1ad9425b84077c.png",
            "sub_url": "https://i0.hdslb.com/bfs/wbi/4932caff0ff746eab6f01bf08b70ac45.png"
        },
        "is_jury": false
    }
}'''
dict_data = json.loads(data)
print(jsonpath.jsonpath(dict_data,'$..img_url'))
# print(dict_data)