
class NumKeys:
    NUM0 = '<96>'
    NUM1 = '<97>'
    NUM2 = '<98>'
    NUM3 = '<99>'
    NUM4 = '<100>'
    NUM5 = '<101>'


class RocketTypeArg:
    HV = '-hvr'  # High velocity rocket
    INC = '-ir'  # Incendiary rocket
    EXP = '-er'  # Explosive rocket


class Language:
    ENG = 0
    RU = 1
    UA = 2


class ColorScheme:
    DEFAULT = 1
    DARK = 2
    LIGHT = 3


class Localization:
    default_lang = Language.RU
    current_lang = default_lang  # add cfg then

    def get_text(template_name):
        return Localization.TextTemplates[template_name][Localization.current_lang]

    TextTemplates = {
        "hide_sight": {
            0: "Hide sight alignment",
            1: "Скрыть прицел для ракетницы"
        },
        "show_high_velocity_rocketsight": {
            0: "Show hight velocity rocket sight",
            1: "Показать прицел для ракет большой дальности"
        },
        "show_incedinary_rocketsight": {
            0: "Show incedinary rocket sight",
            1: "Показать прицел для зажигательных ракет"
        },
        "stop_any_action": {
            0: "Stop any action",
            1: "Остановить все текущие действия"
        },
        "hotkeys_info": {
            0: "Hotkeys",
            1: "Горячие клавиши"
        },
        "show_simple_rocketsight": {
            0: "Sight alignment for regular rocket",
            1: "Прицел для обычных ракет"
        },
        "change_color": {
            0: "Change sight color",
            1: "Изменить цвет прицела"
        },
        "minimize_rust_window": {
            0: "Minimize Rust window",
            1: "Свернуть окно игры"
        },
        "only_for_fixed_resolution": {
            0: "Program works correctly only with 1920x1080 resolution and with borderless window mode",
            1: "Программа работает корректно только с разрешением экрана 1920x1080 и при оконном режиме Borderless(без рамки)"
        },
        "cotact_info": {
            0: "My concacts: andreyperepelytsaaa@gmail.com \nGithub: https://github.com/agdeon",
            1: "Связь со мной: andreyperepelytsaaa@gmail.com\nGithub: https://github.com/agdeon"
        }
    }




