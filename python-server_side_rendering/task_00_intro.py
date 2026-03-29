#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries containing attendee data.

    Returns:
        None
    """

    # --- Validación de tipos ---
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # --- Validación de entradas vacías ---
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- Procesar cada asistente ---
    for idx, attendee in enumerate(attendees, start=1):
        # Reemplazar valores faltantes con "N/A"
        name = attendee.get("name") if attendee.get("name") else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") else "N/A"

        # Crear contenido personalizado
        invitation = template.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))

        # Nombre del archivo de salida
        filename = f"output_{idx}.txt"

        try:
            with open(filename, "w") as f:
                f.write(invitation)
            print(f"Generated {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
