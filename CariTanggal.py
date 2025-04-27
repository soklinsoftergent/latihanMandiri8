import re
from datetime import datetime, date, time, timezone

def format_dan_selisih_tanggal_teks(teks: str):
    LIST_MATCH = re.findall(r"[0-9]{4}-+[0-9]{2}-+[0-9]{2}", teks)
    for match in LIST_MATCH:
        date_object = datetime.fromisoformat(match)
        date_object_now = datetime.now()
        difference = date_object_now - date_object
        print(date_object.strftime("%d-%m-%Y %H:%M:%S"), "selisih", difference.days, "hari")

text = f"""Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02)."""

format_dan_selisih_tanggal_teks(text)

