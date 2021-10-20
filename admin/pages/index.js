/* eslint-disable @next/next/no-html-link-for-pages */
import Head from "next/head"
import { useUser } from "@auth0/nextjs-auth0"
import { Link, Code } from "@geist-ui/react"

export default function Home() {
  const { user, error, isLoading } = useUser()
  if (isLoading) return <div>Loading ...</div>
  if (error) return <div>{error.message}</div>

  return (
    <div>
      <Head>
        <title>Web Event Platform Admin</title>
      </Head>

      {user ? (
        <div>
          <Code block>{JSON.stringify(user, null, 2)}</Code>
          <Link href="/api/auth/logout" color>
            Log out
          </Link>
        </div>
      ) : (
        <Link href="/api/auth/login" color>
          Log in
        </Link>
      )}
    </div>
  )
}
