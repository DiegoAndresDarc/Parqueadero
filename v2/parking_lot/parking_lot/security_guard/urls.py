from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.security_guard_home, name="securityGuardHome"),
    re_path(r'^shift/start/$', views.start_shift, {'action': 'start'}, name="startShift"),
    re_path(r'^shift/end/$', views.end_shift, {'action': 'end'}, name="endShift"),
    re_path(r'^parking-use/barcode/entry/$', views.barcode_parking_place, {'action': 'entry', 'person': 'I'}, name="barcodeIEntry"),
    re_path(r'^parking-use/barcode/departure/$', views.barcode_parking_place, {'action': 'departure', 'person': 'I'}, name="barcodeIDeparture"),
    re_path(r'^parking-use/inhabitant/vehicle/(?P<pk>\d+)/entry/$', views.entry_inhabitant_vehicle, name="entryInhabitantVehicle"),
    re_path(r'^parking-use/inhabitant/vehicle/(?P<parking_place_id>\d+)/departure/$', views.departure_inhabitant_vehicle, name="departureInhabitantVehicle"),
    re_path(r'^parking-use/visitor-id/entry/$', views.visitor_identification, {'action': 'entry'}, name="visitorEntry"),
    re_path(r'^parking-use/visitor-id/departure/$', views.visitor_identification, {'action': 'departure'}, name="visitorDeparture"),
    re_path(r'^visitor/create/$', views.create_visitor, name="visitorCreate"),
    re_path(r'^visitor/(?P<pk>\d+)/vehicles/list/(?P<action>\w+)/$', views.VisitorVehicleListView.as_view(), name="visitorVehicles"),
    re_path(r'^visitor/(?P<pk>\d+)/vehicles/create/$', views.create_visitor_vehicle, name="createVisitorVehicle"),
    re_path(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/parking-barcode/entry/$', views.barcode_parking_place, {'action': 'entry', 'person': 'V'}, name="barcodeVEntry"),
    re_path(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/parking-barcode/departure/$', views.barcode_parking_place, {'action': 'departure', 'person': 'V'}, name="barcodeVDeparture"),
    re_path(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/entry/$', views.entry_visitor_vehicle, name="entryVisitorVehicle"),
    re_path(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/departure/$', views.departure_visitor_vehicle, name="departureVisitorVehicle"),
    re_path(r'^parking-use/visitor/(?P<pk>\d+)/departure/payment/(?P<money>\d+\.\d+)/$', views.make_payment, name="makePayment"),
]