def createData(account):
    data = {}
    data['identifier'] = []
    data['username'] = []
    data['full_name'] = []
    data['profile_pic_url'] = []
    data['profile_pic_url_hd'] = []
    data['biography'] = []
    data['external_url'] = []
    data['follows_count'] = []
    data['followed_by_count'] = []
    data['media_count'] = []
    data['is_private'] = []
    data['is_verified'] = []
    data['blocked_by_viewer'] = []
    data['country_block'] = []
    data['followed_by_viewer'] = []
    data['follows_viewer'] = []
    data['has_channel'] = []
    data['has_blocked_viewer'] = []
    data['highlight_reel_count'] = []
    data['has_requested_viewer'] = []
    data['is_business_account'] = []
    data['is_joined_recently'] = []
    data['business_category_name'] = []
    data['business_email'] = []
    data['business_phone_number'] = []
    data['business_address_json'] = []
    data['requested_by_viewer'] = []
    data['connected_fb_page'] = []
    data['medias'] = []
    data['identifier'] = account.identifier
    data['username'] = account.username
    data['full_name'] = account.full_name
    data['profile_pic_url'] = account.profile_pic_url
    data['profile_pic_url_hd'] = account.profile_pic_url_hd
    data['biography'] = account.biography
    data['external_url'] = account.external_url
    data['follows_count'] = account.follows_count
    data['followed_by_count'] = account.followed_by_count
    data['media_count'] = account.media_count
    data['is_private'] = account.is_private
    data['is_verified'] = account.is_verified
    data['blocked_by_viewer'] = account.blocked_by_viewer
    data['country_block'] = account.country_block
    data['followed_by_viewer'] = account.followed_by_viewer
    data['follows_viewer'] = account.follows_viewer
    data['has_channel'] = account.has_channel
    data['has_blocked_viewer'] = account.has_blocked_viewer
    data['highlight_reel_count'] = account.highlight_reel_count
    data['has_requested_viewer'] = account.has_requested_viewer
    data['is_business_account'] = account.is_business_account
    data['is_joined_recently'] = account.is_joined_recently
    data['business_category_name'] = account.business_category_name
    data['business_email'] = account.business_email
    data['business_phone_number'] = account.business_phone_number
    data['business_address_json'] = account.business_address_json
    data['requested_by_viewer'] = account.requested_by_viewer
    data['connected_fb_page'] = account.connected_fb_page
   
    return data

def addMedia(data, media):
    data['medias'].append({
         'identifier': media.identifier,
         'short_code': media.short_code,
         'created_time': media.created_time,
         'type': media.type,
         'link': media.link,
         'image_low_resolution_url': media.image_low_resolution_url,
         'image_thumbnail_url': media.image_thumbnail_url,
         'image_standard_resolution_url': media.image_standard_resolution_url,
         'image_high_resolution_url': media.image_high_resolution_url,
         'square_images': media.square_images,
         'carousel_media': media.carousel_media,
         'caption': media.caption,
         'is_ad': media.is_ad,
         'video_low_resolution_url': media.video_low_resolution_url,
         'video_standard_resolution_url': media.video_standard_resolution_url,
         'video_low_bandwidth_url': media.video_low_bandwidth_url,
         'video_views': media.video_views,
         'video_url': media.video_url,
   #      'owner': media.owner,
         'likes_count': media.likes_count,
         'location_id': media.location_id,
         'location_name': media.location_name,
         'comments_count': media.comments_count,
         'comments': media.comments,
         'has_more_comments': media.has_more_comments,
         'comments_next_page': media.comments_next_page,
         'location_slug': media.location_slug
      })
    return data
