SQL> 
SQL> SELECT 'INSERT INTO reviews (id, bank_id, review, rating, review_date, source, sentiment_label, sentiment_score) VALUES ('
  2      || id || ', '
  3      || bank_id || ', '''
  4      || REPLACE(REPLACE(SUBSTR(review,1,500),'\'',''''),CHAR(10),' ') || ''', '
  5      || rating || ', TO_DATE('''
  6      || TO_CHAR(review_date, 'YYYY-MM-DD') || ''', ''YYYY-MM-DD''), '''
  7      || source || ''', '''
  8      || sentiment_label || ''', '
  9      || NVL(TO_CHAR(sentiment_score),'NULL') || ');'
 10  FROM reviews;
ERROR:
ORA-01756: quoted string not properly terminated 
Help: https://docs.oracle.com/error-help/db/ora-01756/ 


SQL> 
SQL> SPOOL OFF
