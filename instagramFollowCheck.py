import json

def instagramFollowCheck (file_path1, file_path2):

    # Load the followers
    with open(file_path2, 'r') as file2:
        followerList = json.load(file2)
    
    # Put following into a hashmap
    hash_map = {}

    for follower in followerList:
        for string in follower["string_list_data"]:
            hash_map[string["value"]] = True

    # Load the following
    with open(file_path1, 'r') as file1:
        followingList = json.load(file1)
    
    # Keep track of missing people in following
    not_found = []
    for following in followingList["relationships_following"]:
        for string in following["string_list_data"]:
            if string["value"] not in hash_map:
                not_found.append(string["value"])
    
    return not_found

result = instagramFollowCheck('./followers_and_following/following.json', './followers_and_following/followers_1.json')

# View the results

if result:
    print(f"{'Index':<10}{'Username':<20}")
    print("-" * 30)
    for index, username in enumerate(result, start=1):
        print(f"{index:<10}{username:<20}")
else:
    print("No missing usernames found.")