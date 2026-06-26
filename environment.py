from browser import Browser
from pages.login_page import LoginPage
from pages.categories_page import CategoriesPage
from pages.cart_page import CartPage



def before_scenario(context, scenario):
    context.browser = Browser()

    context.login_page = LoginPage(context.browser.driver)
    context.categories_page = CategoriesPage(context.browser.driver)
    context.cart_page = CartPage(context.browser.driver)

    # Login automat doar pentru scenariile cu tag @categories
    if "categories" in scenario.tags:
        context.login_page.open()
        context.login_page.login("demoblaze", "demoblaze")
        context.login_page.verify_user_menu_button("Welcome demoblaze")

    if "cart" in scenario.tags:
        context.login_page.open()
        context.login_page.login("demoblaze", "demoblaze")
        context.login_page.verify_user_menu_button("Welcome demoblaze")

        context.cart_page.open_cart()
        context.cart_page.clear_cart()
        context.categories_page.click_link_home_page()


def after_scenario(context, scenario):
    if hasattr(context, "browser") and context.browser:
        context.browser.close()
        context.browser = None