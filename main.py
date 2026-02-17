from modules.client_manager import ClientManager
from modules.regular_client import RegularClient
from modules.premium_client import PremiumClient
from modules.corporate_client import CorporateClient

from modules.exceptions import ClientError,InvalidNameError, InvalidEmailError, InvalidPhoneError
from modules.validations import validate_name, validate_email, validate_phone


def print_menu() -> None:
    print("\n=== Menú ===")
    print("1) Agregar cliente")
    print("2) Lista de clientes")
    print("3) Buscar cliente por ID")
    print("4) Buscar cliente por email")
    print("5) Actualizar cliente")
    print("6) Eliminar cliente")
    print("0) Salir")


def prompt_non_empty(label: str) -> str:
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("El input no puede estar vacío. Intenta de nuevo.")

def prompt_unique_client_id(manager: ClientManager, label: str = "ID del cliente (ej: 001)") -> str:
    while True:
        value = prompt_non_empty(label)
        # opcional: si tienes validate_client_id en client.py, no es necesario aquí
        if manager.id_exists(value):
            print(f"[ERROR] Ya existe un cliente con ID {value}. Intenta con otro.\n")
            continue
        return value


def prompt_name(label: str = "Nombre") -> str:
    while True:
        value = prompt_non_empty(label)
        try:
            validate_name(value)
            return value
        except InvalidNameError as e:
            print(f"[ERROR] {e}")
            print("Intenta nuevamente.\n")

def prompt_email(label: str = "Email") -> str:
    while True:
        value = prompt_non_empty(label).lower()
        try:
            validate_email(value)
            return value
        except InvalidEmailError as e:
            print(f"[ERROR] {e}")
            print("Formato esperado: ejemplo@dominio.com\n")


def prompt_phone(label: str = "Teléfono") -> str:
    print("Regla: solo dígitos, entre 8 y 12 caracteres.")
    while True:
        value = prompt_non_empty(label)

        # Feedback inmediato 
        if not value.isdigit():
            print("[ERROR] El teléfono debe contener solo números.\n")
            continue

        length = len(value)
        if length < 8:
            print(f"[ERROR] Teléfono demasiado corto: tiene {length} dígitos. Mínimo 8.\n")
            continue
        if length > 12:
            print(f"[ERROR] Teléfono demasiado largo: tiene {length} dígitos. Máximo 12.\n")
            continue

        # Validación final 
        try:
            validate_phone(value)
            return value
        except InvalidPhoneError as e:
            print(f"[ERROR] {e}\n")


def prompt_client_type() -> str:
    while True:
        print("\nTipo de cliente:")
        print("1) Regular")
        print("2) Premium")
        print("3) Corporativo")
        choice = input("Elige (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("Opción inválida. Intenta de nuevo.")


def create_client_from_input(manager: ClientManager):
    client_type = prompt_client_type()
    client_id = prompt_unique_client_id(manager)
    name = prompt_name("Nombre")
    email = prompt_email("Email")          
    phone = prompt_phone("Teléfono")       
    address = prompt_non_empty("Dirección")

    if client_type == "1":
        return RegularClient(client_id, name, email, phone, address)

    if client_type == "2":
        return PremiumClient(client_id, name, email, phone, address)


    # client_type == "3"
    company_name = prompt_non_empty("Nombre de la empresa")
    return CorporateClient(client_id, name, email, phone, address, company_name=company_name)



def add_client_flow(manager: ClientManager) -> None:
    while True:
        try:
            client = create_client_from_input(manager)
            manager.add_client(client)
            print("\nCliente agregado exitosamente.")
            print(client)
            break
        except ClientError as e:
            print(f"\n[ERROR] {e}")
            print("Intenta nuevamente.\n")


def list_clients_flow(manager: ClientManager) -> None:
    clients = manager.list_clients()
    if not clients:
        print("\n(No hay clientes registrados aún.)")
        return

    print("\n=== LISTA DE CLIENTES ===")
    for c in clients:
        print(c)


def find_by_id_flow(manager: ClientManager) -> None:
    client_id = prompt_non_empty("ID del cliente a buscar")
    client = manager.get_client_by_id(client_id)
    print("\n=== CLIENTE ENCONTRADO ===")
    print(client)


def find_by_email_flow(manager: ClientManager) -> None:
    email = prompt_email("Email a buscar")
    client = manager.get_client_by_email(email)
    print("\n=== CLIENTE ENCONTRADO ===")
    print(client)


def update_client_flow(manager: ClientManager) -> None:
    client_id = prompt_non_empty("ID del cliente a actualizar")
    client = manager.get_client_by_id(client_id)

    print("\nDatos actuales:")
    print(client)
    print("\nDeja vacío para no actualizar.\n")

    new_name = input("Nuevo nombre: ").strip()
    new_email_raw = input("Nuevo email: ").strip()
    new_phone_raw = input("Nuevo teléfono: ").strip()
    new_address = input("Nueva dirección: ").strip()

    updates = {}

    if new_name:
        updates["name"] = new_name

    # Validación inmediata si el usuario intenta cambiar email
    if new_email_raw:
        try:
            validate_email(new_email_raw)
            updates["email"] = new_email_raw.lower()
        except InvalidEmailError as e:
            raise e 

    # Validación inmediata si el usuario intenta cambiar teléfono
    if new_phone_raw:
        if not new_phone_raw.isdigit():
            raise InvalidPhoneError("El teléfono debe contener solo números.")
        if len(new_phone_raw) < 8:
            raise InvalidPhoneError(f"Teléfono demasiado corto: {len(new_phone_raw)} dígitos. Mínimo 8.")
        if len(new_phone_raw) > 12:
            raise InvalidPhoneError(f"Teléfono demasiado largo: {len(new_phone_raw)} dígitos. Máximo 12.")
        validate_phone(new_phone_raw)
        updates["phone"] = new_phone_raw

    if new_address:
        updates["address"] = new_address

    if isinstance(client, PremiumClient):
        new_level = input("Nuevo nivel premium: ").strip()
        if new_level:
            updates["level"] = new_level

    if isinstance(client, CorporateClient):
        new_company = input("Nuevo nombre de empresa: ").strip()
        if new_company:
            updates["company_name"] = new_company

    if not updates:
        print("\n(Ningún cambio realizado.)")
        return

    manager.update_client(client_id, **updates)
    print("\nCliente actualizado exitosamente.")
    print(manager.get_client_by_id(client_id))


def remove_client_flow(manager: ClientManager) -> None:
    client_id = prompt_non_empty("ID del cliente a eliminar")
    client = manager.get_client_by_id(client_id)

    print("\nEstás a punto de eliminar:")
    print(client)
    confirm = input("¿Quieres confirmar la eliminación? (s/n): ").strip().lower()

    if confirm == "s":
        manager.remove_client(client_id)
        print("\nCliente eliminado.")
    else:
        print("\nEliminación cancelada.")


def main():
    manager = ClientManager()

    while True:
        print_menu()
        option = input("Elige una opción: ").strip()

        try:
            if option == "1":
                add_client_flow(manager)
            elif option == "2":
                list_clients_flow(manager)
            elif option == "3":
                find_by_id_flow(manager)
            elif option == "4":
                find_by_email_flow(manager)
            elif option == "5":
                update_client_flow(manager)
            elif option == "6":
                remove_client_flow(manager)
            elif option == "0":
                print("\nAdiós! Vuelve pronto.")
                break
            else:
                print("\nOpción inválida. Intenta de nuevo.")

        except ClientError as e:
            print(f"\n[ERROR] {e}")

        except Exception as e:
            print(f"\n[ERROR INESPERADO] {e}")


if __name__ == "__main__":
    main()
