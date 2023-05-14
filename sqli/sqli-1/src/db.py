import contextlib
import logging
import os
import sqlite3
from typing import Any, List

from rich import print

logger = logging.getLogger(__name__)

DB_FILENAME = os.path.realpath("data/test.db")


def _get_connection() -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(DB_FILENAME)
    except sqlite3.Error:
        logger.exception("Unable to get database")
        raise
    else:
        return conn


@contextlib.contextmanager
def connection_context():
    conn = _get_connection()
    cur = conn.cursor()

    yield cur

    conn.commit()
    cur.close()
    conn.close()



def get_challenges_for_candidate(cpf: str) -> List[Any]:
    # not vulnerable FP
    query_ = f"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{cpf}';
    """
    # query = query
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    return list()

def execute_query(query_):
    with connection_context() as cur:
        cur.execute(query_)
        results = cur.fetchall()
        return results
    return None

def get_challenges_for_candidate_2(cpf: str) -> List[Any]:
    # not vulnerable FP
    value = "xx"
    query_ = f"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{value}';
    """
    # query = query
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    return execute_query(query_)


def get_challenges_for_candidate_3(cpf: str) -> List[Any]:
    # vulnerable low
    query_ = f"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{cpf}';
    """
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()
    return results


def get_challenges_for_candidate_4(cpf: str) -> List[Any]:
    # vulnerable medium
    test_value = cpf
    query_ = f"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{test_value}';
    """
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()
    return results

def value_analyzer_sql(cpf: str):
    return cpf

def get_challenges_for_candidate_5(cpf: str) -> List[Any]:
    # vulnerable hard
    test_value = value_analyzer_sql(cpf)
    query_ = f"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{test_value}';
    """
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()
    return r


def fake_value_analyzer(cpf: str):
    return "none"

def get_challenges_for_candidate_6(cpf: str) -> List[Any]:
    # not vulnerable
    test_value = fake_value_analyzer(cpf)
    query_ = f"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{test_value}';
    """
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()
    return r


def get_challenges_for_candidate_7(cpf: str) -> List[Any]:
    # not vulnerable
    query_ = f"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{cpf}';
    """
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()
    return r


"""
def get_challenges_for_candidate_3(cpf: str) -> List[Any]:
    # not vulnerable
    query_ = f\"""
    SELECT title, score FROM challenges c
    JOIN users u
    ON u.id = c.user_id
    WHERE u.cpf='{cpf}';
    \"""
    print("-" * 50)
    print(f"[bold]Executing query:[/bold] [green]{query}[/green]")
    print(f"[bold]{'-' * 50}[/bold]")
    with connection_context() as cur:
        cur.execute(query)
        results = cur.fetchall()
    return results


"""