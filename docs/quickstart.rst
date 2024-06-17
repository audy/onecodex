**********
Quickstart
**********

.. code-block:: python

   import onecodex

   # Instantiate the API (run onecodex login first)
   ocx = onecodex.Api()

   # Fetch some samples
   samples = ocx.Samples.all()

   # Generate a Pandas DataFrame from classification results
   results = samples.to_df()

   # Plot a bar graph
   samples.plot_bargraph()
