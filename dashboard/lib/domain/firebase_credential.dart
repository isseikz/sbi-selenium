class FirebaseCredential {
  final String clientId;
  FirebaseCredential(this.clientId);

  static loadEnvironment() {
    return FirebaseCredential(
        const String.fromEnvironment("DASHBOARD_FIREBASE_CLIENT_ID"));
  }
}
