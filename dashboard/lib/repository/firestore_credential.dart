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
}
