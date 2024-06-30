from datetime import datetime

schedule = [
    {
        "id": 101,
        "name": "neeraj",
        "meetings": [
            {"with": 102, "from": "2024-06-27 19:00", "to": "2024-06-27 20:00"}
        ],
    },
    {
        "id": 103,
        "name": "hiren",
        "meetings": [
            {"with": 101, "from": "2024-06-27 19:00", "to": "2024-06-27 20:00"}
        ],
    },
]

# print(datetime.now())

to_schedule = {
    "id": 101,
    "name": "neeraj",
    "meetings": [{"with": 102, "from": "2024-06-27 19:00", "to": "2024-06-27 20:00"}],
}


def is_available(people: list, to: datetime, fro: datetime):



is_available([101], "2024-06-27 19:00", "2024-06-27 20:00")


# Problem Statement:

# We need to build a Calendar system, which supports following functionalities:

# Prelim: (Single person)
# Schedule a meeting with input of Day and time and period(or to and from time)
# Should be able to detect any collisions if scheduling a new meeting.

# Advance: (Multiple person, room accommodation)
# include meeting rooms as parameter
# detect if there is collision when scheduling
# include other persons in meeting as parameter
# detect if other person is available

# Interface:
# can be Cmdline, rest API or even JS
# define your contracts, so that we can test
# Evaluation:
# Working Code - highest points
# defining Contracts
# Database Designs
# Database Selection
# Is code adaptable to new changes (OOP or functional your choice)
# Github Submission
# Unit Testing

# create store procedure, trigger, function or view


Data warehouse play crucial role in business environments by maintaining lineage of historical data by creating data models which helps analyst and owners draw insights to take decisions.