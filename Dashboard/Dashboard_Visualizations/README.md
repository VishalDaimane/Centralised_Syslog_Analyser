# How to Add an NDJSON File in OpenSearch Dashboards for Visualizations in Saved Objects

This guide explains how to import an NDJSON file containing saved objects (such as visualizations, dashboards, and index patterns) into OpenSearch Dashboards.

## Steps to Import NDJSON File

1. **Open OpenSearch Dashboards**
   - Navigate to your OpenSearch Dashboards URL (e.g., `http://localhost:5601`).

2. **Go to Dashboard Management**
   - Click on the menu (usually the gear icon) on the left sidebar.
   - Select **Dashboard Management**.

3. **Access Saved Objects**
   - In Dashboard Management, click on **Saved Objects**.

4. **Import the NDJSON File**
   - Click the **Import** button at the top right.
   - In the file dialog, select your NDJSON file containing the saved visualizations.
   - Optionally, check the box to **Automatically overwrite all saved objects** if you want to replace existing objects with the same IDs.
   - Click **Import**.

5. **Verify Imported Objects**
   - After import, you will see a list of imported objects.
   - You can now use these visualizations in your dashboards.

6. **Create or Edit Dashboards**
   - Go to the **Dashboard** section.
   - Create a new dashboard or edit an existing one.
   - Add the imported visualizations to your dashboard.

## Notes

- The NDJSON file is typically exported from OpenSearch Dashboards via the **Export** feature in Saved Objects.
- Make sure the index patterns used by the visualizations exist in your OpenSearch cluster.
- If index patterns are missing, import them first or create them manually.

## Example NDJSON Import Command (CLI)

If you want to import saved objects via the OpenSearch API, you can use the following curl command:



The Example Dashboard :
![Dashboard](/Assests/dashboard.png)
