from modules.client_manager import ClientManager
from modules.regular_client import RegularClient
from modules.premium_client import PremiumClient
from modules.corporate_client import CorporateClient


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


def create_client_from_input():
    client_type = prompt_client_type()

    client_id = prompt_non_empty("Cliente ID")
    name = prompt_non_empty("Nombre")
    email = prompt_non_empty("Email").lower()
    phone = prompt_non_empty("Teléfono")
    address = prompt_non_empty("Dirección")

    if client_type == "1":
        return RegularClient(client_id, name, email, phone, address)

    if client_type == "2":
        level = input("Cliente Premium  (default=Gold): ").strip() or "Gold"
        return PremiumClient(client_id, name, email, phone, address, level=level)

    # client_type == "3"
    company_name = prompt_non_empty("Nombre de la empresa")
    return CorporateClient(client_id, name, email, phone, address, company_name=company_name)


def add_client_flow(manager: ClientManager) -> None:
    client = create_client_from_input()
    manager.add_client(client)
    print("\nCliente agregado exitosamente.")
    print(client)


def list_clients_flow(manager: ClientManager) -> None:
    clients = manager.list_clients()
    if not clients:
        print("\n(No hay clientes registrados aún.)")
        return

    print("\n=== LISTA DE CLIENTES ===")
    for c in clients:
        print(c)


def find_by_id_flow(manager: ClientManager) -> None:
    client_id = prompt_non_empty("Cliente ID a buscar")
    client = manager.get_client_by_id(client_id)
    print("\n=== CLIENTE ENCONTRADO ===")
    print(client)


def find_by_email_flow(manager: ClientManager) -> None:
    email = prompt_non_empty("Email a buscar").lower()
    client = manager.get_client_by_email(email)
    print("\n=== CLIENTE ENCONTRADO ===")
    print(client)


def update_client_flow(manager: ClientManager) -> None:
    client_id = prompt_non_empty("Cliente ID a actualizar")
    client = manager.get_client_by_id(client_id)

    print("\nValores comunes:")
    print(client)
    print("\nMantenlo vacío para no actualizar.\n")

    new_name = input("Nuevo nombre: ").strip()
    new_email = input("Nuevo email: ").strip().lower()
    new_phone = input("Nuevo teléfono: ").strip()
    new_address = input("Nueva dirección: ").strip()

    updates = {}
    if new_name:
        updates["name"] = new_name
    if new_email:
        updates["email"] = new_email
    if new_phone:
        updates["phone"] = new_phone
    if new_address:
        updates["address"] = new_address

    
    if isinstance(client, PremiumClient):
        new_level = input("Nuevo cliente premium: ").strip()
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
    client_id = prompt_non_empty("Cliente ID a eliminar")
    client = manager.get_client_by_id(client_id)

    print("\nEstás a punto de eliminar:")
    print(client)
    confirm = input("Quieres confirmar la eliminación? (s/n): ").strip().lower()

    if confirm == "s":
        manager.remove_client(client_id)
        print("\nCliente eliminado.")
    else:
        print("\nEliminación cancelada.")


def main():
    manager = ClientManager()

    while True:
        print_menu()
        option = input("Elige una opción    : ").strip()

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
                print("\nAdios! Vuelve pronto")
                break
            else:
                print("\nOpción inválida. Intenta de nuevo.")

        except ValueError as e:
            
            print(f"\n[ERROR] {e}")

        except Exception as e:
            # Seguridad básica para evitar que el programa se caiga por errores inesperados
            print(f"\n[ERROR INESPERADO] {e}")


if __name__ == "__main__":
    main()
