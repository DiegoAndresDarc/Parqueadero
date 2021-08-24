from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.security_guard_home, name="securityGuardHome"),
    url(r'^shift/start/$', views.start_shift, {'action': 'start'}, name="startShift"),
    url(r'^shift/end/$', views.end_shift, {'action': 'end'}, name="endShift"),
    url(r'^parking-use/barcode/entry/$', views.barcode_parking_place, {'action': 'entry', 'person': 'I'}, name="barcodeIEntry"),
    url(r'^parking-use/barcode/departure/$', views.barcode_parking_place, {'action': 'departure', 'person': 'I'}, name="barcodeIDeparture"),
    url(r'^parking-use/inhabitant/vehicle/(?P<pk>\d+)/entry/$', views.entry_inhabitant_vehicle, name="entryInhabitantVehicle"),
    url(r'^parking-use/inhabitant/vehicle/(?P<parking_place_id>\d+)/departure/$', views.departure_inhabitant_vehicle, name="departureInhabitantVehicle"),
    url(r'^parking-use/visitor-id/entry/$', views.visitor_identification, {'action': 'entry'}, name="visitorEntry"),
    url(r'^parking-use/visitor-id/departure/$', views.visitor_identification, {'action': 'departure'}, name="visitorDeparture"),
    url(r'^visitor/create/$', views.create_visitor, name="visitorCreate"),
    url(r'^visitor/(?P<pk>\d+)/vehicles/list/(?P<action>\w+)/$', views.VisitorVehicleListView.as_view(), name="visitorVehicles"),
    url(r'^visitor/(?P<pk>\d+)/vehicles/create/$', views.create_visitor_vehicle, name="createVisitorVehicle"),
    url(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/parking-barcode/entry/$', views.barcode_parking_place, {'action': 'entry', 'person': 'V'}, name="barcodeVEntry"),
    url(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/parking-barcode/departure/$', views.barcode_parking_place, {'action': 'departure', 'person': 'V'}, name="barcodeVDeparture"),
    url(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/entry/$', views.entry_visitor_vehicle, name="entryVisitorVehicle"),
    url(r'^parking-use/visitor/vehicle/(?P<pk>\d+)/departure/$', views.departure_visitor_vehicle, name="departureVisitorVehicle"),
    url(r'^parking-use/visitor/(?P<pk>\d+)/departure/payment/(?P<money>\d+\.\d+)/$', views.make_payment, name="makePayment"),
]