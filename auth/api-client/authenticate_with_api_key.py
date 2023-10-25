
# from google.cloud import language_v1


# def authenticate_with_api_key(quota_project_id: str, api_key_string: str) -> None:
#     """
#     Authenticates with an API key for Google Language service.

#     TODO(Developer): Replace these variables before running the sample.

#     Args:
#         quota_project_id: Google Cloud project id that should be used for quota and billing purposes.
#         api_key_string: The API key to authenticate to the service.
#     """

#     # Credentials is saved in C:\Users\User\AppData\Roaming\gcloud\application_default_credentials.json
#     quota_project_id = "helical-element-389100"
    
#     # Change this to your own google cloud token
#     api_key_string = "1//01pgI30nozgKFCgYIARAAGAESNwF-L9Irn7j-r9SDIakGKT1AdhhN7Ej_piGn7b0v1JrYdl_9rxikg4xALfJNIX2r4ZS2R72szuo"

#     # Initialize the Language Service client and set the API key and the quota project id.
#     client = language_v1.LanguageServiceClient(
#         client_options={"api_key": api_key_string, "quota_project_id": quota_project_id}
#     )

#     text = "Hello, world!"
#     document = language_v1.Document(
#         content=text, type_=language_v1.Document.Type.PLAIN_TEXT
#     )

#     # Make a request to analyze the sentiment of the text.
#     sentiment = client.analyze_sentiment(
#         request={"document": document}
#     ).document_sentiment

#     print(f"Text: {text}")
#     print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")
#     print("Successfully authenticated using the API key")
