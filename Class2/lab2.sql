/**
	STATS404 LAB 2
	WI2019
	RITA HSU
**/

--Using the chinook database, find out who were the top 3 most purchased artist in CA each year.;

DROP TABLE IF EXISTS temp.purchases;
CREATE TEMP TABLE purchases AS
SELECT strftime('%Y',invoices.InvoiceDate) AS PurchaseYear
    , artists.ArtistId
    , artists.Name
    , SUM(invoice_items.Quantity) AS QuantityPurchased
FROM artists
    JOIN albums ON artists.ArtistId = albums.ArtistId
    JOIN tracks ON albums.AlbumId = tracks.AlbumId
    JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
    JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    JOIN customers ON invoices.CustomerId = customers.CustomerId
WHERE customers.State = 'CA' OR invoices.BillingState = 'CA'
GROUP BY strftime('%Y',invoices.InvoiceDate)
    , artists.ArtistId
    , artists.Name;

--SELECT *
--FROM purchases
--ORDER BY PurchaseYear, QuantityPurchased DESC;


DROP TABLE IF EXISTS top3;
CREATE TEMP TABLE top3 AS
SELECT p.PurchaseYear, p.ArtistId, p.Name, p.QuantityPurchased
FROM purchases p
WHERE p.ArtistId IN (SELECT q.ArtistId
                        FROM purchases q
                        WHERE p.PurchaseYear = q.PurchaseYear
                        ORDER BY q.QuantityPurchased DESC
                        LIMIT 3);

SELECT *
FROM top3
ORDER BY PurchaseYear, QuantityPurchased DESC;