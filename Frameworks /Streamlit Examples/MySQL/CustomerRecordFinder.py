import streamlit as st
import mysql.connector

def fetch_customer_payments(customer_id, mysql_config):
    """Fetches customer payment information from the MySQL database."""

    try:
        cnx = mysql.connector.connect(**mysql_config)
        cursor = cnx.cursor()

        query = (
            "SELECT * FROM paymentsstatement WHERE CustomerID = %s"
        )
        cursor.execute(query, (customer_id,))

        payment_records = cursor.fetchall()

        return payment_records

    except mysql.connector.Error as err:
        st.error(f"Error connecting to MySQL: {err}")
        return []  # Return an empty list in case of an error

    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()


def main():
    st.title("Customer Service Payment Assistant")

    # Input for Customer ID
    customer_id = st.text_input("Enter Customer ID:")

    # MySQL Connection Configuration (Replace with your actual credentials)
    mysql_config = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'your_database'
    }

    # Fetch and Display Payment Information
    if customer_id:
        payment_records = fetch_customer_payments(customer_id, mysql_config)
        if payment_records:
            st.subheader("Payment History:")
            for record in payment_records:
                st.write(f"- **Payment ID:** {record[0]}, **Date:** {record[2]}, **Amount:** ${record[3]:.2f}, **Status:** {record[5]}, **Notes:** {record[6]}")
        else:
            st.info(f"No payments found for customer {customer_id}")


if __name__ == "__main__":
    main()
