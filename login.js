export async function onRequestPost(context) {
    const { request, env } = context;
    const { password } = await request.json();

    // 🔒 ULTIMATE SECURITY: We pull the hashes from your Dashboard Settings.
    // They are NO LONGER in the code files.
    const DEV_HASH = env.DEV_HASH;
    const ADMIN_HASH = env.ADMIN_HASH;

    if (!DEV_HASH || !ADMIN_HASH) {
        return new Response(JSON.stringify({ success: false, message: "System not configured" }), {
            status: 500,
            headers: { "Content-Type": "application/json" }
        });
    }

    // Helper to hash the incoming password
    const msgUint8 = new TextEncoder().encode(password);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashedInput = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

    let role = "user";
    if (hashedInput === DEV_HASH) role = "dev";
    else if (hashedInput === ADMIN_HASH) role = "admin";

    if (role !== "user") {
        return new Response(JSON.stringify({ success: true, role }), {
            headers: { "Content-Type": "application/json" }
        });
    }

    return new Response(JSON.stringify({ success: false, message: "Invalid Key" }), {
        status: 401,
        headers: { "Content-Type": "application/json" }
    });
}
