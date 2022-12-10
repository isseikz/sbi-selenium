import 'package:dashboard/domain/firebase_credential.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:google_sign_in/google_sign_in.dart';

class AuthenticationService {
  final FirebaseAuth _auth;
  final FirebaseCredential _cred;

  AuthenticationService(this._auth, this._cred);

  Future<void> signInWithGoogle() async {
    final googleUser = await GoogleSignIn(clientId: _cred.clientId).signIn();

    final googleAuth = await googleUser?.authentication;
    if (googleAuth != null) {
      final credential = GoogleAuthProvider.credential(
        accessToken: googleAuth.accessToken,
        idToken: googleAuth.idToken,
      );
      await _auth.signInWithCredential(credential);
    }
  }
}
