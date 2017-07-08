==========
Quickstart
==========

1. Add dappr to your urlpatterns::

.. code-block:: python
	
	from dappr import urls

	urlpatterns = [
		...
		url(r'^registration/', include(urls)),
	]

2. Create a link to dappr's registration view

.. code-block:: html

	...(some template)...
	<a href="{% url 'registration_view' %}">Create an account</a>

3. That's it! Everything from the link click onwards will be taken care of by sensible defaults.

.. note::
	To customize the registration process, subclass and modify one of the :doc:`provided views <views>`