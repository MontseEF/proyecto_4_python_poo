import csv
import os
from typing import List

from modules.client import Client
from modules.regular_client import RegularClient
from modules.premium_client import PremiumClient
from modules.corporate_client import CorporateClient

CSV_PATH = "data/clients.csv"
REPORT_PATH = "reports/report.txt"

FIELDNAMES = ["tipo", "id_cliente", "nombre", "email", "teléfono", "dirección", "nombre_empresa"]


def save_clients_to_csv(clients: List[Client]) -> None:
    os.makedirs("data", exist_ok=True)

    with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()

        for client in clients:
            row = client.to_dict()

            # Completar claves faltantes
            for key in FIELDNAMES:
                row.setdefault(key, "")

            # Escribir SOLO columnas esperadas
            writer.writerow({k: row[k] for k in FIELDNAMES})


def load_clients_from_csv() -> List[Client]:
    if not os.path.exists(CSV_PATH):
        return []

    clients: List[Client] = []

    with open(CSV_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            client_type = (row.get("tipo") or "Regular").strip()

            client_id = (row.get("id_cliente") or "").strip()
            name = (row.get("nombre") or "").strip()
            email = (row.get("email") or "").strip()
            phone = (row.get("teléfono") or "").strip()
            address = (row.get("dirección") or "").strip()
            company_name = (row.get("nombre_empresa") or "").strip()

            
            if not client_id or not name or not email:
                continue

            if client_type.lower() in ("corporativo", "corporate"):
                client = CorporateClient(
                    client_id, name, email, phone, address, company_name=company_name
                )
            elif client_type.lower() in ("premium",):
                client = PremiumClient(client_id, name, email, phone, address)
            else:
                client = RegularClient(client_id, name, email, phone, address)

            clients.append(client)

    return clients


def generate_report_txt(clients: List[Client]) -> None:
    os.makedirs("reports", exist_ok=True)

    with open(REPORT_PATH, mode="w", encoding="utf-8") as file:
        file.write("REPORTE DE CLIENTES\n")
        file.write("===================\n\n")
        file.write(f"Total clientes: {len(clients)}\n\n")

        for client in clients:
            file.write(str(client) + "\n")


def generate_report_txt(clients: List[Client]) -> None:
    os.makedirs("reports", exist_ok=True)

    with open(REPORT_PATH, mode="w", encoding="utf-8") as file:
        file.write("REPORTE DE CLIENTES\n")
        file.write("===================\n\n")
        file.write(f"Total clientes: {len(clients)}\n\n")

        for client in clients:
            file.write(str(client) + "\n")
