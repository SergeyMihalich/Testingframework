from Base.Login import Login
from pom.FiltersPage import FilterPage
from pom.HomePageNavigation import HomePageNavigation


hpn = HomePageNavigation()
Filter = FilterPage()

Login().login()

assert hpn.get_navigation_links_text() == hpn.navigation_links_in_page, "вкладки на странице не совпадают ожидаемым"

hpn.payment_calendar()
Filter.check_filter()