class FirestoreCredential {
  final String apiKey;
  final String authDomain;
  final String appId;
  final String messagingSenderId;
  final String projectId;
  final String storageBucket;

  FirestoreCredential(this.apiKey, this.authDomain, this.appId,
      this.messagingSenderId, this.projectId, this.storageBucket) {
    if (apiKey.isEmpty) throw ArgumentError.value(apiKey);
    if (authDomain.isEmpty) throw ArgumentError.value(apiKey);
    if (appId.isEmpty) throw ArgumentError.value(apiKey);
    if (messagingSenderId.isEmpty) throw ArgumentError.value(apiKey);
    if (projectId.isEmpty) throw ArgumentError.value(apiKey);
    if (storageBucket.isEmpty) throw ArgumentError.value(apiKey);
  }

  static loadEnvironment() {
    return FirestoreCredential(
        const String.fromEnvironment("DASHBOARD_FIRESTORE_API_KEY"),
        const String.fromEnvironment("DASHBOARD_FIRESTORE_AUTH_DOMAIN"),
        const String.fromEnvironment("DASHBOARD_FIRESTORE_APP_ID"),
        const String.fromEnvironment("DASHBOARD_FIRESTORE_MSG_SENDER_ID"),
        const String.fromEnvironment("DASHBOARD_FIRESTORE_PROJECT_ID"),
        const String.fromEnvironment("DASHBOARD_FIRESTORE_STORAGE_BUCKET"));
  }
}
