=========
Templates
=========

.. |br| raw:: html

   <br />

Email Templates
-----------------
Override these files to define your own custom HTML content to be sent in the notification emails.

.. note::
  For more information on overriding templates, visit the `Django docs <https://docs.djangoproject.com/en/1.11/howto/overriding-templates/>`_

Confirmation email
~~~~~~~~~~~~~~~~~~
The message that allows the user to confirm their email address.

**Email body template**

.. raw:: html

    <table border="1" class="docutils">
      <thead>
        <tr>
          <th class="head">Filename</th>
          <th class="head">Context</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code class="code docutils literal">'registration/confirmation_email.html'</code></td>
          <td>
            <table class="docutils">
              <tr>
                <td><b><code class="code docutils literal">site</code></b></td>
                <td>The current instance of <a href="https://docs.djangoproject.com/en/1.11/ref/contrib/sites/#django.contrib.sites.models.Site">Site</a> providing details about your website</td>
              </tr>
              <tr>
                <td><b><code class="code docutils literal">conf_key</code></b></td>
                <td>An alphanumeric string to be plugged in to the 
                  <code class="code docutils literal">confirmation_view</code> 
                  url to create a unique identification link</td>
              </tr>
            </table>
          </td>
        </tr>
      </tbody>
    </table>

**Email subject template**

.. raw:: html

    <table border="1" class="docutils">
      <thead>
        <tr>
          <th class="head">Filename</th>
          <th class="head">Context</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code class="code docutils literal">'registration/confirmation_email_subject.txt'</code></td>
          <td>
            <table class="docutils no-margin">
              <tr>
                <td><b><code class="code docutils literal">site</code></b></td>
                <td>The current instance of <a href="https://docs.djangoproject.com/en/1.11/ref/contrib/sites/#django.contrib.sites.models.Site">Site</a> providing details about your website</td>
              </tr>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
