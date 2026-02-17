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

            # Asegurar columnas fijas aunque falten en algunos tipos
            for key in FIELDNAMES:
                if key not in row:
                    row[key] = ""

            # Escribir SOLO las claves esperadas
            writer.writerow({k: row[k] for k in FIELDNAMES})


def load_clients_from_csv() -> List[Client]:
    if not os.path.exists(CSV_PATH):
        return []

    clients: List[Client] = []

    with open(CSV_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            client_type = (row.get("type") or "Regular").strip()

            client_id = (row.get("client_id") or "").strip()
            name = (row.get("name") or "").strip()
            email = (row.get("email") or "").strip()
            phone = (row.get("phone") or "").strip()
            address = (row.get("address") or "").strip()
            company_name = (row.get("company_name") or "").strip()

            if client_type == "Corporate":
                client = CorporateClient(client_id, name, email, phone, address, company_name=company_name)
            elif client_type == "Premium":
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
