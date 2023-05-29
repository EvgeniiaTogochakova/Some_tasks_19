import text
import view
import model


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))

            case 5:
                name_to_find = view.ask_what_name_to_find(text.ask_what_name_to_find, text.name_in_name,
                                                          text.surname_in_name, text.cancel_input)
                one_contact = model.find_contact(name_to_find)
                view.print_one_contact(text.successful_search, text.unsuccessful_search, one_contact)

            case 6:
                name_to_find = view.ask_what_name_to_find(text.ask_what_name_to_change, text.name_in_name,
                                                          text.surname_in_name, text.cancel_input)
                one_contact = model.find_contact(name_to_find)
                view.print_one_contact(text.successful_search, text.unsuccessful_search, one_contact)
                a = view.confirmation(text.confirmation)
                new_contact = view.to_get_new_data(a, text.how_to_change_name, text.how_to_change_phone,
                                                   text.how_to_change_comment)
                model.change_contact(a, one_contact, new_contact, model.path)
                view.after_changing(a, text.after_changing_file, text.no_changing)

            case 7:
                pb = model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                break
