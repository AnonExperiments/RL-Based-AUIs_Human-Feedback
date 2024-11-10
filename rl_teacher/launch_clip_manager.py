import argparse
from rl_teacher.clip_manager import ClipManager
from rl_teacher.utils import slugify


def main(args=None):
    domain = args.domain
    user_id = args.user_id
    env_id = args.env_id
    experiment_name = slugify(args.name)

    workers = args.workers

    print("Starting the clip manager for:\n\t user_id: ", user_id, "domain: ", domain, " - env_id: ", env_id)
    clip_manager = ClipManager(None, env_id, experiment_name, 1, user_id=user_id, domain=domain, training=False)

    if clip_manager.total_number_of_clips > 0 and not clip_manager._sorted_clips:
            # If there are clips but no sort tree, create a sort tree!
            print("If there are clips but no sort tree, create a sort tree!")
            clip_manager.create_new_sort_tree_from_existing_clips()
    clip_manager.sort_clips(wait_until_database_fully_sorted=True)

    print("Clip manager completed!.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--env_id', required=True)
    parser.add_argument('-d', '--domain', required=False, type=str)
    parser.add_argument('-u', '--user_id', required=False, type=int)
    parser.add_argument('-w', '--workers', default=4, type=int)
    parser.add_argument('-n', '--name', required=True)
    args = parser.parse_args()

    main(args=args)