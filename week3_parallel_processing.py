# python3

from collections import namedtuple
from queue import PriorityQueue

WorkerAvailability = namedtuple("WorkerAvailability", ["available_time", "worker_id"])
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = PriorityQueue()

     # Initialize all workers with starting free time of 0
    for worker in range(n_workers):
        next_free_time.put(WorkerAvailability(0, worker))

    # Process each job and assign it to the next available worker
    for job in jobs:
        next_worker = next_free_time.get()
        worker_index = next_worker.worker_id
        start_time = next_worker.available_time

        result.append(AssignedJob(worker_index, start_time))

        # Update worker's next free time after completing the assigned job
        new_free_time = start_time + job
        next_free_time.put(WorkerAvailability(new_free_time, worker_index))
    return result


def main():
     # Read input for number of workers and number of jobs
    n_workers, n_jobs = map(int, input().split())

     # Read job durations
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # Assign jobs and retrieve assigned job details
    assigned_jobs = assign_jobs(n_workers, jobs)

    # Print assigned jobs with worker and start time
    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
