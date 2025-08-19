import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
const = getFirestore(app);

async function logLoginAttempt(email, status, errorMessage = null) {
  try {
    await addDoc(collection(db, "loginLogs"), {
      email: email,
      status: status, // "success" or "failure"
      timestamp: serverTimestamp(),
      error: errorMessage
    });
  } catch (logError) {
    console.error("Failed to log login attempt:", logError);
  }
}
