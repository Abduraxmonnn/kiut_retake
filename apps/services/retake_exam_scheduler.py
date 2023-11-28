# cls RetakeExamScheduler
# func schedule_retake_exams


def schedule_retake_exams(student: object, subject: object) -> bool:
    """
    Schedules retake exams for students who failed their subjects.

    This function takes a list of students and a list of subjects as input. For each student, it checks which
    subjects they failed. For each failed subject, it assigns a room, time, and date for the retake exam. Finally,
    it adds the retake exam to the student's schedule.

    Args:
        student (object): A student objects. Each student object should have a `failed_subject` method that
                        takes a subject object as input and returns `True` if the student failed that subject,
                        and `False` otherwise.
        subject (object): A subject objects.

    Returns:
        bool: `True` if all retake exams were successfully scheduled, `False` otherwise.

    Raises:
        ValueError: If the `students` or `subjects` argument is not a list.
        ValueError: If any of the student objects in the `students` list do not have a `failed_subject` method.
    """
    pass
