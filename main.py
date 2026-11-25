#!/usr/bin/env python3
"""Have You Tried Turning It Off? — satu baris tech support.

Baris juara arena sesi ini (lihat ARENA.md di luar repo):

    Have you tried turning it off and on again? I have — seven times
    today, and the printer's fine. I'm the one who needs a restart now.

132 karakter, satu baris. Belokannya: agen sudah melakukan langkah klasik
itu tujuh kali — dan yang ternyata rusak adalah agennya sendiri, bukan
printer pelanggan. Pelanggan bukan bahan tertawaan; yang ditertawakan
adalah ketidakberdayaan agen yang ceria. Keputusasaan pelanggan terasa
lewat "seven times today" tanpa perlu dijelaskan.

Program deterministik, tanpa jaringan, tanpa acak, tanpa masukan luar:
menulis baris itu persis seperti di atas ke berkas keluaran, tanpa baris
baru di akhir, supaya hitungan karakternya tetap 132.
"""

import os

LINE = (
    "Have you tried turning it off and on again? I have "
    "\u2014 seven times today, and the printer's fine. "
    "I'm the one who needs a restart now."
)


def output_path():
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return os.path.join(override, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main():
    assert 1 <= len(LINE) <= 199, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    data = LINE.encode("utf-8")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
