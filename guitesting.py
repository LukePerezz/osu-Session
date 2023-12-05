import dearpygui.dearpygui as dpg

def print_me(sender):
    print(f"Menu item: {sender}")

dpg.create_context()
dpg.create_viewport(title="osu!Session Analyzer", width=800, height=600)
dpg.setup_dearpygui()

with dpg.window(label="Main", width=800, height=600, tag="Primary Window"):
    with dpg.menu_bar():
        with dpg.menu(label="Menu"):
            dpg.add_menu_item(label="Session Details", callback=print_me, id=1)
            dpg.add_menu_item(label="Account", callback=print_me, id=2)
        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="graphics", callback=print_me, id=3)
            dpg.add_menu_item(label="audio", callback=print_me, id=4)

dpg.show_viewport()
while dpg.is_dearpygui_running():

    dpg.set_primary_window("Primary Window", True)
    dpg.render_dearpygui_frame()

dpg.destroy_context()
