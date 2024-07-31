def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, (int, float)):
        return None
    online_users = 0
    for initial_t, exit_t in permanence_period:
        if not isinstance(initial_t, (int)) or not isinstance(exit_t, (int)):
            return None
        if initial_t <= target_time <= exit_t:
            online_users += 1
    return online_users
