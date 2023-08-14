import logging
import requests


class GeoDBCitiesRESTClient:

    def __init__(self, api_key, api_host="wft-geo-db.p.rapidapi.com"):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.base_url = "https://{}/v1".format(api_host)
        self.default_headers = {"X-RapidAPI-Key": api_key,
                                "X-RapidAPI-Host": api_host}
        self._session = requests.Session()

    def __del__(self):
        self._session.close()

    def __repr__(self):
        return "Client for https://wirefreethought.github.io/geodb-cities-api-docs/"

    def _request(self, method, request_path, headers=None, params=None, **kwargs):
        full_url = self.base_url + '/' + request_path
        if headers is not None:
            headers.update(self.default_headers)
        else:
            headers = self.default_headers
        self.logger.debug("Sending {} request to {}\nHeaders: {}\nBody: {}\n".format(method, full_url, headers,
                                                                                     kwargs.get('data', '')))
        response = self._session.request(method, full_url, headers=headers, params=params, **kwargs)
        self.logger.debug("Getting response from {}\nCode: {}\nHeaders: {}\nBody: {}\n".format(response.url,
                                                                                               response.status_code,
                                                                                               response.headers,
                                                                                               response.text))
        return response

    def get(self, request_path, headers=None, params=None, **kwargs):
        return self._request('GET', request_path, headers=headers, params=params, **kwargs)

    # ----- Geo ----- #
    def get_admin_divisions(self, **kwargs):
        """Find administrative divisions, filtering by optional criteria.

        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find administrative divisions")
        path = "geo/adminDivisions"
        return self.get(path, params=kwargs)

    def get_admin_division_details(self, division_id):
        """Get administrative division details.

        :param division_id: ID of admin division

        :return: API response
        """
        self.logger.info("Get administrative division [{}] details".format(division_id))
        path = "geo/adminDivisions/{}".format(division_id)
        return self.get(path)

    def get_cities_near_division(self, division_id, **kwargs):
        """Find cities near the given administrative division, filtering by optional criteria.

        :param division_id: ID of admin division
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find cities near administrative division [{}]".format(division_id))
        path = "geo/adminDivisions/{}/nearbyCities".format(division_id)
        return self.get(path, params=kwargs)

    def get_admin_divisions_near_division(self, division_id, **kwargs):
        """Find administrative divisions near the given division, filtering by optional criteria.

        :param division_id: ID of admin division
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find administrative divisions near administrative division [{}]".format(division_id))
        path = "geo/adminDivisions/{}/nearbyDivisions".format(division_id)
        return self.get(path, params=kwargs)

    def get_places_near_division(self, division_id, **kwargs):
        """Find places near the given administrative division, filtering by optional criteria.

        :param division_id: ID of admin division
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find places near administrative division [{}]".format(division_id))
        path = "geo/adminDivisions/{}/nearbyPlaces".format(division_id)
        return self.get(path, params=kwargs)

    def get_cities(self, **kwargs):
        """Find cities, filtering by optional criteria.

        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find cities")
        path = "geo/cities"
        return self.get(path, params=kwargs)

    def get_cities_near_city(self, city_id, **kwargs):
        """Find cities near the given city, filtering by optional criteria.

        :param city_id: ID of the city
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find cities near city [{}]".format(city_id))
        path = "geo/cities/{}/nearbyCities"
        return self.get(path, params=kwargs)

    def get_admin_divisions_near_city(self, city_id, **kwargs):
        """Find administrative divisions near the given city, filtering by optional criteria.

        :param city_id: ID of the city
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find administrative divisions near city [{}]".format(city_id))
        path = "geo/cities/{}/nearbyDivisions".format(city_id)
        return self.get(path, params=kwargs)

    def get_places_near_city(self, city_id, **kwargs):
        """Find places near the given city, filtering by optional criteria.

        :param city_id: ID of the city
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find places near city [{}]".format(city_id))
        path = "geo/cities/{}/nearbyPlaces".format(city_id)
        return self.get(path, params=kwargs)

    def get_city_details(self, city_id, **kwargs):
        """Get city details.

        :param city_id: ID of the city
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get city [{}] details".format(city_id))
        path = "geo/cities/{}".format(city_id)
        return self.get(path, params=kwargs)

    def get_city_distance(self, city_id, to_city_id, **kwargs):
        """Get distance from the given city.

        :param city_id: ID of the city
        :param to_city_id: ID of the city distance is measured to
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get distance from city [{}] to city [{}]".format(city_id, to_city_id))
        path = "geo/cities/{}/distance?toCityId={}".format(city_id, to_city_id)
        return self.get(path, params=kwargs)

    def get_city_datetime(self, city_id):
        """Get city date-time.

        :param city_id: ID of the city

        :return: API response
        """
        self.logger.info("Get city [{}] date-time".format(city_id))
        path = "geo/cities/{}/dateTime".format(city_id)
        return self.get(path)

    def get_city_containing_region(self, city_id, **kwargs):
        """Get the details for the containing populated place.

        :param city_id: ID of the city
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get the details of region that contains city [{}]".format(city_id))
        path = "geo/cities/{}/locatedIn".format(city_id)
        return self.get(path, params=kwargs)

    def get_city_time(self, city_id):
        """Get city time.

        :param city_id: ID of the city

        :return: API response
        """
        self.logger.info("Get city [{}] time".format(city_id))
        path = "geo/cities/{}/time".format(city_id)
        return self.get(path)

    def get_countries(self, **kwargs):
        """Find countries, filtering by optional criteria.

        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find countries")
        path = "geo/countries"
        return self.get(path, params=kwargs)

    def get_country_details(self, country_id, **kwargs):
        """Get country details.

        :param country_id: an ISO-3166 country code or WikiData id
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get country [{}] details".format(country_id))
        path = "geo/countries/{}".format(country_id)
        return self.get(path, params=kwargs)

    def get_country_places(self, country_id, **kwargs):
        """Get the country's places.

        :param country_id: an ISO-3166 country code or WikiData id
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get country [{}] places".format(country_id))
        path = "geo/countries/{}/places".format(country_id)
        return self.get(path, params=kwargs)

    def get_country_regions(self, country_id, **kwargs):
        """Get the country's regions.

        :param country_id: an ISO-3166 country code or WikiData id
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get country [{}] regions".format(country_id))
        path = "geo/countries/{}/regions".format(country_id)
        return self.get(path, params=kwargs)

    def get_region_details(self, country_id, region_code, **kwargs):
        """Get country region details.

        :param country_id: an ISO-3166 country code or WikiData id
        :param region_code: an ISO-3166 or FIPS region code
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get country [{}], region [{}] details".format(country_id, region_code))
        path = "geo/countries/{}/regions/{}".format(country_id, region_code)
        return self.get(path, params=kwargs)

    def get_country_region_admin_divisions(self, country_id, region_code, **kwargs):
        """Get country region administrative divisions.

        :param country_id: an ISO-3166 country code or WikiData id
        :param region_code: an ISO-3166 or FIPS region code
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get country [{}], region [{}] administrative divisions".format(country_id, region_code))
        path = "geo/countries/{}/regions/{}/adminDivisions".format(country_id, region_code)
        return self.get(path, params=kwargs)

    def get_country_region_cities(self, country_id, region_code, **kwargs):
        """Get country region cities.

        :param country_id: an ISO-3166 country code or WikiData id
        :param region_code: an ISO-3166 or FIPS region code
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get country [{}], region [{}] cities".format(country_id, region_code))
        path = "geo/countries/{}/regions/{}/cities".format(country_id, region_code)
        return self.get(path, params=kwargs)

    def get_country_region_places(self, country_id, region_code, **kwargs):
        """Get country region places.

        :param country_id: an ISO-3166 country code or WikiData id
        :param region_code: an ISO-3166 or FIPS region code
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get country [{}], region [{}] places".format(country_id, region_code))
        path = "geo/countries/{}/regions/{}/places".format(country_id, region_code)
        return self.get(path, params=kwargs)

    def get_cities_near_location(self, location_id, **kwargs):
        """Find cities near the given location, filtering by optional criteria.

        :param location_id: a latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find cities near location [{}]".format(location_id))
        path = "geo/locations/{}/nearbyCities".format(location_id)
        return self.get(path, params=kwargs)

    def get_admin_divisions_near_location(self, location_id, **kwargs):
        """Find administrative divisions near the given location, filtering by optional criteria.

        :param location_id: a latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find administrative divisions near location [{}]".format(location_id))
        path = "geo/locations/{}/nearbyDivisions".format(location_id)
        return self.get(path, params=kwargs)

    def get_places_near_location(self, location_id, **kwargs):
        """Find places near the given location, filtering by optional criteria.

        :param location_id: a latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find places near location [{}]".format(location_id))
        path = "geo/locations/{}/nearbyPlaces".format(location_id)
        return self.get(path, params=kwargs)

    def get_places(self, **kwargs):
        """Find places, filtering by optional criteria.

        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find places")
        path = "geo/places"
        return self.get(path, params=kwargs)

    def get_places_near_place(self, place_id, **kwargs):
        """Find places near the given place, filtering by optional criteria.

        :param place_id: a place id (either native 'id' or 'wikiDataId')
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find places near place [{}]".format(place_id))
        path = "geo/places/{}/nearbyPlaces".format(place_id)
        return self.get(path, params=kwargs)

    def get_place_details(self, place_id, **kwargs):
        """Get place details.

        :param place_id: a place id (either native 'id' or 'wikiDataId')
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get place [{}] details".format(place_id))
        path = "geo/places/{}".format(place_id)
        return self.get(path, params=kwargs)

    def get_place_distance(self, place_id, to_place_id, **kwargs):
        """Get distance from the given place.

        :param place_id: a place id (either native 'id' or 'wikiDataId')
        :param to_place_id: id of a place distance is measured to
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get distance from place [{}] to [{}]".format(place_id, to_place_id))
        path = "geo/places/{}/distance?toPlaceId={}".format(place_id, to_place_id)
        return self.get(path, params=kwargs)

    def get_place_datetime(self, place_id):
        """Get place date-time.

        :param place_id: a place id (either native 'id' or 'wikiDataId')

        :return: API response
        """
        self.logger.info("Get place [{}] datetime".format(place_id))
        path = "geo/places/{}/dateTime".format(place_id)
        return self.get(path)

    def get_place_containing_region(self, place_id, **kwargs):
        """Get the details for the containing populated place.

        :param place_id: a place id (either native 'id' or 'wikiDataId')
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get the details for the containing populated place [{}]".format(place_id))
        path = "geo/places/{}/locatedIn".format(place_id)
        return self.get(path, params=kwargs)

    def get_place_time(self, place_id):
        """Get place time.

        :param place_id: a place id (either native 'id' or 'wikiDataId')

        :return: API response
        """
        self.logger.info("Get place [{}] time".format(place_id))
        path = "geo/places/{}/time".format(place_id)
        return self.get(path)

    # ----- Locale ----- #
    def get_currencies(self, country_id, **kwargs):
        """Find currencies, filtering by optional criteria.

        :param country_id: an ISO-3166 country code or WikiData id
        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Find currencies for country [{}]".format(country_id))
        path = "locale/currencies?countryId={}".format(country_id)
        return self.get(path, params=kwargs)

    def get_languages(self, **kwargs):
        """Get all supported languages.

        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get all supported languages")
        path = "locale/languages"
        return self.get(path, params=kwargs)

    def get_locales(self, **kwargs):
        """Get all known locales.

        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get all supported locales")
        path = "locale/locales"
        return self.get(path, params=kwargs)

    def get_timezones(self, **kwargs):
        """Get all known time-zones.

        :param kwargs: optional query parameters for filtering

        :return: API response
        """
        self.logger.info("Get all supported timezones")
        path = "locale/timezones"
        return self.get(path, params=kwargs)

    def get_timezone(self, zone_id):
        """Get time-zone.

        :param zone_id: a time-zone id

        :return: API response
        """
        self.logger.info("Get timezone")
        path = "locale/timezones/{}".format(zone_id)
        return self.get(path)

    def get_timezone_datetime(self, zone_id):
        """Get time-zone date-time.

        :param zone_id: a time-zone id

        :return: API response
        """
        self.logger.info("Get timezone datetime")
        path = "locale/timezones/{}/dateTime".format(zone_id)
        return self.get(path)

    def get_timezone_time(self, zone_id):
        """Get time-zone time.

        :param zone_id: a time-zone id

        :return: API response
        """
        self.logger.info("Get timezone time")
        path = "locale/timezones/{}/time".format(zone_id)
        return self.get(path)


if __name__ == "__main__":
    cl = GeoDBCitiesRESTClient("")
    resp = cl.get_cities_near_division(3301438)
    print(resp.json())
