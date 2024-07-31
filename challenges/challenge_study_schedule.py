def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, (int, float)):
        return None
    online_users = 0
    
    for initial_time, exit_time in permanence_period:
        if not isinstance(initial_time, (int, float)) or not isinstance(exit_time, (int, float)):
            return None
        if initial_time <= target_time <= exit_time:
            online_users += 1
    return online_users
