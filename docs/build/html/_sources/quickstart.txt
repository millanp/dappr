==========
Quickstart
==========
1. Add dappr to your urlpatterns::

	from dappr import urls

	urlpatterns = [
		...
		url(r'^registration/', include(urls)),
	]

2. Create a link to dappr's registration view

.. code-block:: html

		...(some template)...
		<a href="{% url 'registration_view' %}">Create an account</a>