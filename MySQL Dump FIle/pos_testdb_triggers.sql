
-- Holiday Discount Trigger
DELIMITER //
CREATE TRIGGER holiday_discount BEFORE INSERT ON pos_testdb.transactions
FOR EACH ROW
BEGIN

IF transactions.date_added BETWEEN 11/20/YEAR(GETDATE()) AND 11/26/YEAR(GETDATE())
THEN UPDATE pos_testdb.transactions SET pos_testdb.transactions.subtotal = transactions.subtotal * 0.90;
END IF;

--  Vendor Alert Trigger
DELIMITER //
CREATE TRIGGER vendor_alert AFTER UPDATE ON products
FOR EACH ROW BEGIN
	IF products.amount < 50 THEN 
		UPDATE vendor
			SET vendor.need_order = True;

END //