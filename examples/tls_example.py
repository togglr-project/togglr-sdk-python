#!/usr/bin/env python3
"""Example of using TLS certificates in togglr-sdk-python."""

from togglr import Client, ClientConfig, RequestContext


def main():
    """Demonstration of various ways to configure TLS."""
    
    print("=== TLS Configuration Examples in togglr-sdk-python ===\n")
    
    # Example 1: Using with_ methods
    print("1. Configuration via with_ methods:")
    config1 = ClientConfig.default("42b6f8f1-630c-400c-97bd-a3454a07f700") \
        .with_base_url("https://localhost") \
        .with_ssl_ca_cert("/path/to/ca-certificate.pem") \
        .with_client_cert("/path/to/client-cert.pem", "/path/to/client-key.pem") \
        .with_tls_server_name("api.togglr.com") \
        .with_ssl_hostname_verification(True)
    
    print(f"   Base URL: {config1.base_url}")
    print(f"   CA Certificate: {config1.ssl_ca_cert}")
    print(f"   Client Certificate: {config1.cert_file}")
    print(f"   Client Key: {config1.key_file}")
    print(f"   TLS Server Name: {config1.tls_server_name}")
    print(f"   Hostname Verification: {config1.assert_hostname}")
    
    # Example 2: Using new_client with parameters
    print("\n2. Configuration via new_client with parameters:")
    from togglr.client import new_client
    client2 = new_client(
        "42b6f8f1-630c-400c-97bd-a3454a07f700",
        base_url="https://localhost",
        ssl_ca_cert="/path/to/ca-certificate.pem",
        cert_file="/path/to/client-cert.pem",
        key_file="/path/to/client-key.pem",
        ca_cert_data="-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
        tls_server_name="api.togglr.com",
        assert_hostname=True
    )
    
    print(f"   Base URL: {client2.config.base_url}")
    print(f"   CA Certificate: {client2.config.ssl_ca_cert}")
    print(f"   Client Certificate: {client2.config.cert_file}")
    print(f"   Client Key: {client2.config.key_file}")
    print(f"   CA Certificate Data: {client2.config.ca_cert_data[:50]}...")
    print(f"   TLS Server Name: {client2.config.tls_server_name}")
    print(f"   Hostname Verification: {client2.config.assert_hostname}")
    
    # Example 3: Insecure mode (for testing)
    print("\n3. Insecure mode (for testing only):")
    config3 = ClientConfig.default("42b6f8f1-630c-400c-97bd-a3454a07f700") \
        .with_base_url("https://localhost") \
        .with_insecure()  # Disables SSL certificate verification
    
    print(f"   Base URL: {config3.base_url}")
    print(f"   Insecure Mode: {config3.insecure}")
    print(f"   SSL Verification: {not config3.insecure}")
    
    # Example 4: Using CA data instead of file
    print("\n4. Using CA data as string:")
    ca_cert_data = """-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKoK/Ovj8uU4MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApTb21lLVN0YXRlMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQwHhcNMTkwOTEyMjE1MjAyWhcNMjkwOTA5MjE1MjAyWjBF
...
-----END CERTIFICATE-----"""
    
    config4 = ClientConfig.default("42b6f8f1-630c-400c-97bd-a3454a07f700") \
        .with_base_url("https://localhost") \
        .with_ca_cert_data(ca_cert_data)
    
    print(f"   Base URL: {config4.base_url}")
    print(f"   CA Certificate Data: {config4.ca_cert_data[:50]}...")
    
    print("\n=== All examples configured! ===")
    print("\nNotes:")
    print("- Replace '42b6f8f1-630c-400c-97bd-a3454a07f700' with your actual API key")
    print("- Specify correct paths to certificates")
    print("- For production use secure settings (not insecure)")
    print("- TLS Server Name (SNI) should match the server name in the certificate")


if __name__ == "__main__":
    main()
