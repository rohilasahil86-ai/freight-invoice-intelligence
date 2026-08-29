
-- Freight & invoice intelligence system for Bussiness Analysis queries.

-- 1 Total Records
SELECT COUNT(*) AS total_records
FROM freight_invoice_cleaned;

-- 2. Total Unique Vendors
SELECT COUNT(DISTINCT Vendor_ID) AS total_vendors
FROM freight_invoice_cleaned;

-- 3. Origin and Destination Cities
SELECT 
    COUNT(DISTINCT Origin_City) AS total_origin_cities,
    COUNT(DISTINCT Destination_City) AS total_destination_cities
FROM freight_invoice_cleaned;


-- 4. Shipment Date Range
SELECT 
    MIN(Shipment_Date) AS first_shipment_date,
    MAX(Shipment_Date) AS last_shipment_date
FROM freight_invoice_cleaned;


-- 5. Invoice Date Range
SELECT 
    MIN(Invoice_Date) AS first_invoice_date,
    MAX(Invoice_Date) AS last_invoice_date
FROM freight_invoice_cleaned;


-- 6. Transport Mode Distribution
SELECT 
    Transport_Mode,
    COUNT(*) AS total_shipments
FROM freight_invoice_cleaned
GROUP BY Transport_Mode;


-- 7. Average Freight Cost by Transport Mode
SELECT 
    Transport_Mode,
    AVG(Total_Freight_Cost) AS avg_freight_cost
FROM freight_invoice_cleaned
GROUP BY Transport_Mode;


-- 8. Vendor with Most Shipments
SELECT 
    Vendor_Name,
    COUNT(*) AS total_shipments
FROM freight_invoice_cleaned
GROUP BY Vendor_Name
ORDER BY total_shipments DESC
LIMIT 1;


-- 9. Vendor with Highest Average Freight Cost
SELECT 
    Vendor_Name,
    AVG(Total_Freight_Cost) AS avg_freight_cost
FROM freight_invoice_cleaned
GROUP BY Vendor_Name
ORDER BY avg_freight_cost DESC
LIMIT 1;


-- 10. Vendor with Highest Average Fraud Risk Score
SELECT 
    Vendor_Name,
    AVG(Fraud_Risk_Score) AS avg_fraud_risk_score
FROM freight_invoice_cleaned
GROUP BY Vendor_Name
ORDER BY avg_fraud_risk_score DESC
LIMIT 1;


-- 11. Invoice Mismatch Distribution
SELECT 
    Invoice_Mismatch_Flag,
    COUNT(*) AS total_invoices
FROM freight_invoice_cleaned
GROUP BY Invoice_Mismatch_Flag;


-- 12. Duplicate Invoice Distribution
SELECT 
    Duplicate_Invoice_Flag,
    COUNT(*) AS total_invoices
FROM freight_invoice_cleaned
GROUP BY Duplicate_Invoice_Flag;


-- 13. Unusual Cost Distribution
SELECT 
    Unusual_Cost_Flag,
    COUNT(*) AS total_shipments
FROM freight_invoice_cleaned
GROUP BY Unusual_Cost_Flag;


-- 14. High-Risk Vendor Distribution
SELECT 
    High_Risk_Vendor_Flag,
    COUNT(*) AS total_shipments
FROM freight_invoice_cleaned
GROUP BY High_Risk_Vendor_Flag;


-- 15. Risk Level Distribution
SELECT 
    Risk_Level,
    COUNT(*) AS total_records
FROM freight_invoice_cleaned
GROUP BY Risk_Level;


-- 16. Payment Status Distribution
SELECT 
    Payment_Status,
    COUNT(*) AS total_records
FROM freight_invoice_cleaned
GROUP BY Payment_Status;


-- 17. Average Payment Delay by Status
SELECT 
    Payment_Status,
    AVG(Payment_Delay_Days) AS avg_payment_delay
FROM freight_invoice_cleaned
GROUP BY Payment_Status;