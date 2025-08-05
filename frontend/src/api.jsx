const API_URL = 'http://localhost:8000/analyze';

export async function uploadImage(imageFile) {
  const formData = new FormData();
  formData.append('file', imageFile);

  const response = await fetch(API_URL, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const err = await response.json();
    throw new Error(err.error || 'Upload failed');
  }

  return response.json();
}
